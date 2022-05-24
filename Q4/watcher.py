from spf import dijkstra
from create_flows import create_flows
import numpy as np
import requests
import os
from requests.auth import HTTPBasicAuth
import time
from send_flows import send_flows


def delete_flows(A):
    n = A.shape[0]
    for i in range(n):
        os.system(f"ovs-ofctl del-flows -O OpenFlow13 s{i+1}")

def watcher(A, password):
    n = A.shape[0]
    B = np.zeros((n, n), int) # An array for saving the port numbers that connets switches
    B[0,0] = 1 # First port of s1 is for h1
    B[-1,-1] = 1 # First port of sn is for h2
    added = []
    for i in range(n):
        for j in range(n):
            if A[i,j] != 0 and (i,j) not in added and (j,i) not in added:
                B[i,j] = np.max(B[i,:])+1
                B[j,i] = np.max(B[j,:])+1
                added.append((i,j))
    cnt = 1
    t = time.time()
    C = A.copy()
    while(True):
        if time.time()-t>=1:
            process = False
            D = A.copy()
            url = "http://127.0.0.1:8181/restconf/operational/opendaylight-inventory:nodes"
            response = requests.get(url, auth=HTTPBasicAuth('admin', 'admin'))
            for node in response.json()["nodes"]["node"]:
                node_id = node["id"].split(':')[1]
                for link in node["node-connector"]:
                    link_id = link["id"].split(':')[2]
                    is_down = link["flow-node-inventory:state"]["link-down"]
                    if is_down and link_id != 'LOCAL':
                        process = True
                        for i in range(B[int(node_id)-1,:].size):
                            if B[int(node_id)-1][i] == int(link_id):
                                D[int(node_id)-1][i] = 0
                                break
            if process:
                C = D.copy()
                delete_flows(A)
                os.system(f"echo {password} | sudo -S rm -rf flows{node_id}{link_id}")
                create_flows(A, f'flows{node_id}{link_id}', C)
                send_flows(f"flows{node_id}{link_id}")
                process = False
            t = time.time()
        with open('check.txt', 'r') as file:
            if file.read() == 'False':
                break

if __name__=='__main__':
    print("Enter number of switches: ", end='')
    n = int(input())
    print("Enter the matrix: ")
    A = np.array([input().strip().split() for _ in range(n)], int)
    print("Please enter your password: ", end='')
    password = input()
    watcher(A, password)