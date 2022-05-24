import numpy as np
from asyncio import protocols
from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink
import os
from create_flows import create_flows
from send_flows import send_flows
from watcher import watcher

def topology(A):
    n = A.shape[0]

    net = Mininet(
        controller = RemoteController,
        switch = OVSKernelSwitch,
        link = TCLink
    )

    # Adding hosts
    h1 = net.addHost(name='h1', ip='10.0.1.1/24', mac='00:00:00:00:00:01')
    h2 = net.addHost(name='h2', ip='10.0.2.1/24', mac='00:00:00:00:00:02')

    # Adding switches
    switches = [] # A list for saving switches
    for i in range(n):
        switches.append(net.addSwitch(name=f's{i+1}', protocols='OpenFlow13'))
    

    # Adding links
    net.addLink(h1, switches[0])
    net.addLink(h2, switches[n-1])
    added = []
    for i in range(n):
        for j in range(n):
            if A[i,j] != 0 and (i,j) not in added and (j,i) not in added:
                net.addLink(switches[i], switches[j])
                added.append((i, j))

    # Adding controller
    c = net.addController(name='c', ip='127.0.0.1', port=6653)

    for s in switches:
        s.start([c])

    net.build()
    net.start()

    # Adding gateways to the hosts
    h1.cmd("route add default gw 10.0.1.1")
    h2.cmd("route add default gw 10.0.2.1")

    # Deleting flows of l2-switch
    for i in range(n):
        switches[i].cmd(f"ovs-ofctl del-flows -O OpenFlow13 s{i+1}")
    
    send_flows('flows')

    CLI(net)
    net.stop()
    with open("check.txt", 'w') as file:
        file.write('False')

if __name__=='__main__':
    print("Enter number of switches: ", end='')
    n = int(input())
    print("Enter the matrix: ")
    A = np.array([input().strip().split() for _ in range(n)], int)
    with open("check.txt", 'w') as file:
        file.write("True")
    create_flows(A, 'flows', A)
    topology(A)
