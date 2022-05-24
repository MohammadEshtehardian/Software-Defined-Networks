from mininet.topo import Topo

class MyTopo(Topo):
    "Topology of Question1-Part1"

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost(name='h1', ip='10.0.0.1', mac='00:00:00:00:00:01')
        h2 = self.addHost(name='h2', ip='10.0.0.2', mac='00:00:00:00:00:02')
        h3 = self.addHost(name='h3', ip='10.0.0.3', mac='00:00:00:00:00:03')
        h4 = self.addHost(name='h4', ip='10.0.0.4', mac='00:00:00:00:00:04')
        h5 = self.addHost(name='h5', ip='10.0.0.5', mac='00:00:00:00:00:05')
        h6 = self.addHost(name='h6', ip='10.0.0.6', mac='00:00:00:00:00:06')
        h7 = self.addHost(name='h7', ip='10.0.0.7', mac='00:00:00:00:00:07')
        h8 = self.addHost(name='h8', ip='10.0.0.8', mac='00:00:00:00:00:08')
        s1 = self.addSwitch(name='s1')
        s2 = self.addSwitch(name='s2')
        s3 = self.addSwitch(name='s3')
        s4 = self.addSwitch(name='s4')
        s5 = self.addSwitch(name='s5')
        s6 = self.addSwitch(name='s6')
        s7 = self.addSwitch(name='s7')

        # Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(h5, s3)
        self.addLink(h6, s3)
        self.addLink(h7, s4)
        self.addLink(h8, s4)
        self.addLink(s1, s5)
        self.addLink(s2, s5)
        self.addLink(s3, s6)
        self.addLink(s4, s6)
        self.addLink(s5, s7)
        self.addLink(s6, s7)


topos = { 'mytopo': ( lambda: MyTopo() ) }
