"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
	
        Swth1 = self.addSwitch( 's1' )
        Swth2 = self.addSwitch( 's2' )
	Swth3 = self.addSwitch( 's3' )
        Hos1 = self.addHost( 'h1' )
        Hos2 = self.addHost( 'h2' )
	Hos3 = self.addHost( 'h3' )
	Hos4 = self.addHost( 'h4' )
	Hos5 = self.addHost( 'h5' )
	Hos6 = self.addHost( 'h6' )
	Hos7 = self.addHost( 'h7' )
	Hos8 = self.addHost( 'h8' )
        # Add links
        self.addLink( Hos1, Swth1 )
	self.addLink( Hos2, Swth1 )
	self.addLink( Hos3, Swth2 )
	self.addLink( Hos4, Swth2 )
	self.addLink( Hos5, Swth2 )
	self.addLink( Hos6, Swth3 )
	self.addLink( Hos7, Swth3 )
	self.addLink( Hos8, Swth3 )
        self.addLink( Swth1, Swth2 )
        self.addLink( Swth2, Swth3 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
