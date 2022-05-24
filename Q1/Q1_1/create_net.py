from mininet.topo import Topo

class MyTopo(Topo):
    "Topology of Question1-Part1"

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost(name='Host1', ip='10.0.0.1/24')
        h2 = self.addHost(name='Host2', ip='10.0.0.2/24')
        s1 = self.addSwitch(name='S1')
        s2 = self.addSwitch(name='S2')

        # Add links
        self.addLink(h1, s1)
        self.addLink(s1, s2)
        self.addLink(s2, h2)


topos = { 'mytopo': ( lambda: MyTopo() ) }

