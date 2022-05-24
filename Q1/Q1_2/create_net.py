from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def topology():
    net = Mininet(
        controller = None,
        switch = OVSKernelSwitch,
        link = TCLink
    )

    # Adding hosts
    h1 = net.addHost(name='h1', ip='10.0.1.1/24', mac='00:00:00:00:00:01')
    h2 = net.addHost(name='h2', ip='10.0.2.1/24', mac='00:00:00:00:00:02')

    # Adding switches
    s1 = net.addSwitch(name='s1')
    s2 = net.addSwitch(name='s2')
    r1 = net.addSwitch(name='r1') # router

    # Adding links
    net.addLink(h1, s1)
    net.addLink(s1, r1)
    net.addLink(r1, s2)
    net.addLink(s2, h2)

    net.build()
    net.start()

    # Adding gateways to the hosts
    h1.cmd("route add default gw 10.0.1.1")
    h2.cmd("route add default gw 10.0.2.1")

    CLI(net)
    net.stop()

if __name__=='__main__':
    topology()
