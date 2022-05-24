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
    h1 = net.addHost(name='h1', ip='10.0.0.1', mac='00:00:00:00:00:01')
    h2 = net.addHost(name='h2', ip='10.0.0.2', mac='00:00:00:00:00:02')
    h3 = net.addHost(name='h3', ip='10.0.0.3', mac='00:00:00:00:00:03')

    # Adding switches
    s1 = net.addSwitch(name='s1', protocols="OpenFlow13")
    s2 = net.addSwitch(name='s2', protocols="OpenFlow13")
    s3 = net.addSwitch(name='s3', protocols="OpenFlow13")

    # Adding links
    net.addLink(h1, s1)
    net.addLink(s1, s2)
    net.addLink(h2, s2)
    net.addLink(s2, s3)
    net.addLink(s3, h3)

    net.build()
    net.start()
    CLI(net)
    net.stop()

if __name__=='__main__':
    topology()
