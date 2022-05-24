import json
import os

os.mkdir('flows')

# Flows for s1
# ovs-ofctl add-flow s1 priority=1,arp,actions=flood
s1_arp = {
    "flow": [
        {
            "id": "2",
            "match": {
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
                                        "output-node-connector": "FLOOD"
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

with open('flows/s1_arp.json', 'w') as outfile:
    json.dump(s1_arp, outfile)

# ovs-ofctl add-flow s1 priority=65535,ip,in_port=1,actions=output:2
s1_in1 = {
    "flow": [
        {
            "id": "3",
            "match": {
                "in-port": "1",
                "ethernet-match":{
                    "ethernet-type":{
                        "type": "2048"
                    }
                }
            },
            "cookie_mask": "0",
            "priority": "65535",
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
                                        "output-node-connector": "2"
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

with open('flows/s1_in1.json', 'w') as outfile:
    json.dump(s1_in1, outfile)

# ovs-ofctl add-flow s1 priority=65535,ip,in_port=2,actions=output:1
s1_in2 = {
    "flow": [
        {
            "id": "4",
            "match": {
                "in-port": "2",
                "ethernet-match":{
                    "ethernet-type":{
                        "type": "2048"
                    }
                }
            },
            "cookie_mask": "0",
            "priority": "65535",
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
                                        "output-node-connector": "1"
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

with open('flows/s1_in2.json', 'w') as outfile:
    json.dump(s1_in2, outfile)


# Flows for s2
# ovs-ofctl add-flow s2 priority=1,arp,actions=flood
s2_arp = {
    "flow": [
        {
            "id": "2",
            "match": {
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
                                        "output-node-connector": "FLOOD"
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

with open('flows/s2_arp.json', 'w') as outfile:
    json.dump(s2_arp, outfile)

# ovs-ofctl add-flow s2 priority=65535,ip,in_port=1,actions=output:2
s2_in1 = {
    "flow": [
        {
            "id": "3",
            "match": {
                "in-port": "1",
                "ethernet-match":{
                    "ethernet-type":{
                        "type": "2048"
                    }
                }
            },
            "cookie_mask": "0",
            "priority": "65535",
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
                                        "output-node-connector": "2"
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

with open('flows/s2_in1.json', 'w') as outfile:
    json.dump(s2_in1, outfile)

# ovs-ofctl add-flow s2 priority=65535,ip,in_port=2,actions=output:1
s2_in2 = {
    "flow": [
        {
            "id": "4",
            "match": {
                "in-port": "2",
                "ethernet-match":{
                    "ethernet-type":{
                        "type": "2048"
                    }
                }
            },
            "cookie_mask": "0",
            "priority": "65535",
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
                                        "output-node-connector": "1"
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

with open('flows/s2_in2.json', 'w') as outfile:
    json.dump(s2_in2, outfile)

# Flows for r1
# ovs-ofctl add-flow r1 priority=1,arp,actions=flood
s3_arp = {
    "flow": [
        {
            "id": "2",
            "match": {
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
                                        "output-node-connector": "FLOOD"
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

with open('flows/s3_arp.json', 'w') as outfile:
    json.dump(s3_arp, outfile)

# ovs-ofctl add-flow r1 priority=65535,ip,nw_dst=10.0.2.1/24,actions=dec_ttl,output:2
s3_in1 = {
    "flow": [
        {
            "id": "3",
            "match": {
                "ipv4-destination": "10.0.2.1/32",
                "ethernet-match":{
                    "ethernet-type":{
                        "type": "2048"
                    }
                }
            },
            "cookie_mask": "0",
            "priority": "65535",
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
                                        "output-node-connector": "2"
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

with open('flows/s3_in1.json', 'w') as outfile:
    json.dump(s3_in1, outfile)

# ovs-ofctl add-flow r1 priority=65535,ip,nw_dst=10.0.1.1/24,actions=dec_ttl,output:1
s3_in2 = {
    "flow": [
        {
            "id": "4",
            "match": {
                "ipv4-destination": "10.0.1.1/32",
                "ethernet-match":{
                    "ethernet-type":{
                        "type": "2048"
                    }
                }
            },
            "cookie_mask": "0",
            "priority": "65535",
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
                                        "output-node-connector": "1"
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

with open('flows/s3_in2.json', 'w') as outfile:
    json.dump(s3_in2, outfile)