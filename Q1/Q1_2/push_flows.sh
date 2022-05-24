# Adding flows to the switches
ovs-ofctl add-flow s1 priority=1,arp,actions=flood # Handling arp packets
ovs-ofctl add-flow s1 priority=65535,in_port=1,actions=output:2
ovs-ofctl add-flow s1 priority=65535,in_port=2,actions=output:1
ovs-ofctl add-flow s2 priority=1,arp,actions=flood
ovs-ofctl add-flow s2 priority=65535,in_port=1,actions=output:2
ovs-ofctl add-flow s2 priority=65535,in_port=2,actions=output:1
ovs-ofctl add-flow r1 priority=1,arp,actions=flood
ovs-ofctl add-flow r1 priority=65535,ip,nw_dst=10.0.2.1/24,actions=dec_ttl,output:2 # Checking L3 headers and decrementing TTL
ovs-ofctl add-flow r1 priority=65535,ip,nw_dst=10.0.1.1/24,actions=dec_ttl,output:1
