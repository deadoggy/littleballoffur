import networkx as nx


from littleballoffur.exploration_sampling import LoopErasedRandomWalkSampler, BreadthFirstSearchSampler, DepthFirstSearchSampler

from littleballoffur.exploration_sampling import CommunityStructureExpansionSampler, CirculatedNeighborsRandomWalkSampler, SnowBallSampler
from littleballoffur.exploration_sampling import RandomWalkSampler, MetropolisHastingsRandomWalkSampler, CommonNeighborAwareRandomWalkSampler
from littleballoffur.exploration_sampling import NonBackTrackingRandomWalkSampler, RandomWalkWithRestartSampler, ForestFireSampler

from littleballoffur.exploration_sampling import ShortestPathSampler, RandomWalkWithJumpSampler, FrontierSampler, RandomNodeNeighborSampler

#-----------------------------------#
# TESTS FOR SPANNING TREE SAMPLERS. #
#-----------------------------------#


def test_loop_erased_random_walk_sampler():
    """
    Testing the number of nodes, connectivity and tree structure.
    """
    sampler = LoopErasedRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges()+1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)


def test_breadth_first_search_sampler():
    """
    Testing the number of nodes, connectivity and tree structure.
    """
    sampler = BreadthFirstSearchSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges()+1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)


def test_depth_first_search_sampler():
    """
    Testing the number of nodes, connectivity and tree structure.
    """
    sampler = DepthFirstSearchSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert new_graph.number_of_edges()+1 == new_graph.number_of_nodes()
    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)

#----------------------------------------#
# TESTS FOR CONNECTED SUBGRAPH SAMPLERS. #
#----------------------------------------#

def test_community_structure_expansion_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = CommunityStructureExpansionSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)


def test_circulated_neighbors_random_walk_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = CirculatedNeighborsRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 2, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)


def test_snowball_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = SnowBallSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)


def test_random_walk_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = RandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)


def test_metropolis_hastings_random_walk_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = MetropolisHastingsRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)


def test_common_neighbor_aware_random_walk_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = CommonNeighborAwareRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)


def test_non_back_trackin_random_walk_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = NonBackTrackingRandomWalkSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)


def test_random_walk_with_restart_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = RandomWalkWithRestartSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0.5)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)


def test_forest_fire_sampler():
    """
    Testing the number of nodes and the connectivity.
    """
    sampler = ForestFireSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()
    assert nx.is_connected(new_graph)

#---------------------------------------#
# TESTS FOR UNCONNECTED GRAPH SAMPLERS  #
#---------------------------------------#

def test_shortest_path_sampler():
    """
    Testing the number of nodes.
    """
    sampler = ShortestPathSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()


def test_random_walk_with_jump_sampler():
    """
    Testing the number of nodes.
    """
    sampler = RandomWalkWithJumpSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()


def test_frontier_sampler():
    """
    Testing the number of nodes.
    """
    sampler = FrontierSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes == new_graph.number_of_nodes()


def test_random_node_neighbor_sampler():
    """
    Testing the number of nodes.
    """
    sampler = RandomNodeNeighborSampler()

    graph = nx.watts_strogatz_graph(200, 10, 0)

    new_graph = sampler.sample(graph)

    assert sampler.number_of_nodes <= new_graph.number_of_nodes()
