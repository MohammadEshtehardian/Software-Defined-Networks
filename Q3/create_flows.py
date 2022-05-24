from spf import dijkstra
import numpy as np
import os
import json

def create_flows(A):
    n = A.shape[0]
    os.mkdir('flows')
    path_1_to_n, path_n_to_1 = dijkstra(A)
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
    for i in range(len(path_1_to_n)):
        s = path_1_to_n[i]
        cnt = s+1

        # Finding in_port and out_port for switches with help of paths that we find with dijkstra
        in_port = ''
        out_port = ''
        if cnt==1:
            in_port = '1' # packets from the host 1
            out_port = f"{B[0,path_1_to_n[1]]}"
        elif cnt==n:
            in_port = f"{B[-1,path_1_to_n[-2]]}"
            out_port = '1' # packets send to host 2
        else:
            in_port = f"{B[i,path_1_to_n[i-1]]}"
            out_port = f"{B[i,path_1_to_n[i+1]]}"

        arp = {
            "flow": [
                {
                    "id": "2",
                    "match": {
                        "in-port": in_port,
                        "arp-target-transport-address": "10.0.2.1/32",
                        "ethernet-match":{
                            "ethernet-type":{
                                "type": "2054"
                            }
                        }
                    },
                    "cookie_mask": "0",
                    "priority": "1",
                    "idle-timeout": "0",
                    "hard-timeout": "0",
                    "cookie": "0",
                    "table_id": "0",
                    "opendaylight-flow-statistics:flow-statistics": {
                        "packet-count": "1",
                        "byte-count": "70",
                        "duration": {
                            "second": "839",
                            "nanosecond": "911000000"
                        }
                    },
                    "instructions": {
                        "instruction": [
                            {
                                "order": 0,
                                "apply-actions": {
                                    "action": [
                                        {
                                            "order": 0,
                                            "output-action": {
                                                "max-length": 65535,
                                                "output-node-connector": out_port
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        }
        with open(f'flows/{cnt}_1.json', 'w') as outfile:
            json.dump(arp, outfile)

        ip = {
            "flow": [
                {
                    "id": "3",
                    "match": {
                        "in-port": in_port,
                        "ipv4-destination": "10.0.2.1/32",
                        "ethernet-match":{
                            "ethernet-type":{
                                "type": "2048"
                            }
                        }
                    },
                    "cookie_mask": "0",
                    "priority": "1",
                    "idle-timeout": "0",
                    "hard-timeout": "0",
                    "cookie": "0",
                    "table_id": "0",
                    "opendaylight-flow-statistics:flow-statistics": {
                        "packet-count": "1",
                        "byte-count": "70",
                        "duration": {
                            "second": "839",
                            "nanosecond": "911000000"
                        }
                    },
                    "instructions": {
                        "instruction": [
                            {
                                "order": 0,
                                "apply-actions": {
                                    "action": [
                                        {
                                            "order": 0,
                                            "output-action": {
                                                "max-length": 65535,
                                                "output-node-connector": out_port
                                            }
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            ]
        }
        with open(f'flows/{cnt}_2.json', 'w') as outfile:
            json.dump(ip, outfile)


        for i in range(len(path_n_to_1)):
            s = path_n_to_1[i]
            cnt = s+1

            in_port = ''
            out_port = ''
            if cnt==1:
                in_port = f"{B[0,path_n_to_1[-2]]}"
                out_port = "1" # packets send to host 1
            elif cnt==n:
                in_port = "1" # packets from host 2
                out_port = f"{B[-1,path_n_to_1[1]]}"
            else:
                in_port = f"{B[i,path_n_to_1[i-1]]}"
                out_port = f"{B[i,path_n_to_1[i+1]]}"

            arp = {
                "flow": [
                    {
                        "id": "4",
                        "match": {
                            "in-port": in_port,
                            "arp-target-transport-address": "10.0.1.1/32",
                            "ethernet-match":{
                                "ethernet-type":{
                                    "type": "2054"
                                }
                            }
                        },
                        "cookie_mask": "0",
                        "priority": "1",
                        "idle-timeout": "0",
                        "hard-timeout": "0",
                        "cookie": "0",
                        "table_id": "0",
                        "opendaylight-flow-statistics:flow-statistics": {
                            "packet-count": "1",
                            "byte-count": "70",
                            "duration": {
                                "second": "839",
                                "nanosecond": "911000000"
                            }
                        },
                        "instructions": {
                            "instruction": [
                                {
                                    "order": 0,
                                    "apply-actions": {
                                        "action": [
                                            {
                                                "order": 0,
                                                "output-action": {
                                                    "max-length": 65535,
                                                    "output-node-connector": out_port
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
            with open(f'flows/{cnt}_3.json', 'w') as outfile:
                json.dump(arp, outfile)

            ip = {
                "flow": [
                    {
                        "id": "5",
                        "match": {
                            "in-port": in_port,
                            "ipv4-destination": "10.0.1.1/32",
                            "ethernet-match":{
                                "ethernet-type":{
                                    "type": "2048"
                                }
                            }
                        },
                        "cookie_mask": "0",
                        "priority": "1",
                        "idle-timeout": "0",
                        "hard-timeout": "0",
                        "cookie": "0",
                        "table_id": "0",
                        "opendaylight-flow-statistics:flow-statistics": {
                            "packet-count": "1",
                            "byte-count": "70",
                            "duration": {
                                "second": "839",
                                "nanosecond": "911000000"
                            }
                        },
                        "instructions": {
                            "instruction": [
                                {
                                    "order": 0,
                                    "apply-actions": {
                                        "action": [
                                            {
                                                "order": 0,
                                                "output-action": {
                                                    "max-length": 65535,
                                                    "output-node-connector": out_port
                                                }
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
            with open(f'flows/{cnt}_4.json', 'w') as outfile:
                json.dump(ip, outfile)