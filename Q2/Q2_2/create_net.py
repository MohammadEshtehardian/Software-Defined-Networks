from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def topology():
    net = Mininet(
        controller = RemoteController,
        switch = OVSKernelSwitch,
        link = TCLink
    )

    # Adding hosts
    h1 = net.addHost(name='h1', ip='10.0.1.1/24', mac='00:00:00:00:00:01')
    h2 = net.addHost(name='h2', ip='10.0.2.1/24', mac='00:00:00:00:00:02')

    # Adding switches
    s1 = net.addSwitch(name='s1', protocols="OpenFlow13")
    s2 = net.addSwitch(name='s2', protocols="OpenFlow13")
    s3 = net.addSwitch(name='s3', protocols="OpenFlow13") # router

    # Adding links
    net.addLink(h1, s1)
    net.addLink(s1, s3)
    net.addLink(s3, s2)
    net.addLink(s2, h2)

    # Adding controller
    c = net.addController(name='c', ip='127.0.0.1', port=6653)

    s1.start([c])
    s2.start([c])
    s3.start([c])

    net.build()
    net.start()

    # Adding gateways to the hosts
    h1.cmd("route add default gw 10.0.1.1")
    h2.cmd("route add default gw 10.0.2.1")

    # Deleting flows of l2-switch
    s1.cmd("ovs-ofctl del-flows -O OpenFlow13 s1")
    s2.cmd("ovs-ofctl del-flows -O OpenFlow13 s2")
    s3.cmd("ovs-ofctl del-flows -O OpenFlow13 s3")

    CLI(net)
    net.stop()

if __name__=='__main__':
    topology()
