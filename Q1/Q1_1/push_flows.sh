ovs-ofctl add-flow S1 in_port="S1-eth1",actions=output:"S1-eth2"
ovs-ofctl add-flow S1 in_port="S1-eth2",actions=output:"S1-eth1"
ovs-ofctl add-flow S2 in_port="S2-eth1",actions=output:"S2-eth2"
ovs-ofctl add-flow S2 in_port="S2-eth2",actions=output:"S2-eth1"