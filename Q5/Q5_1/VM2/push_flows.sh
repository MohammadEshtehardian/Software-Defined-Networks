ovs-ofctl add-flow -O OpenFlow13 s2 in_port=1,actions=set_field:100-\>tunnel_id,output:3
ovs-ofctl add-flow -O OpenFlow13 s2 in_port=2,actions=set_field:200-\>tunnel_id,output:3
ovs-ofctl add-flow -O OpenFlow13 s2 table=0,in_port=3,tunnel_id=100,actions=goto_table:1
ovs-ofctl add-flow -O OpenFlow13 s2 table=1,actions=output:1
ovs-ofctl add-flow -O OpenFlow13 s2 table=0,in_port=3,tunnel_id=200,actions=goto_table:2
ovs-ofctl add-flow -O OpenFlow13 s2 table=2,actions=output:2
ovs-vsctl add-port s2 v -- set interface v type=vxlan option:key=flow ofport_request=3 option:remote_ip=192.168.237.128