from asyncio import protocols
from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink
import os


def topology():

    net = Mininet(
        controller = None,
        switch = OVSKernelSwitch,
        link = TCLink
    )

    # Adding hosts
    h1 = net.addHost(name='h1g', ip='10.0.0.1/24', mac='00:00:00:00:00:01')
    h2 = net.addHost(name='h1b', ip='10.0.0.1/24', mac='00:00:00:00:00:02')

    s1 = net.addSwitch(name='s1', protocols='OpenFlow13')

    net.addLink(h1, s1)
    net.addLink(h2, s1)

    net.build()
    net.start()
    CLI(net)
    net.stop()

if __name__=='__main__':
    topology()
