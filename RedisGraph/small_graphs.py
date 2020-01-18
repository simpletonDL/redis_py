from redisgraph import Graph, Node, Edge
from redis import Redis


def create_simple(r: Redis):
    g = Graph('simple', r)

    v0 = Node(label='v0')
    v1 = Node(label='v1')
    v2 = Node(label='v2')
    v3 = Node(label='v3')
    v4 = Node(label='v4')

    g.add_node(v0)
    g.add_node(v1)
    g.add_node(v2)
    g.add_node(v3)
    g.add_node(v4)

    e1 = Edge(v0, 'r0', v1)
    e2 = Edge(v1, 'r1', v2)
    e3 = Edge(v2, 'r0', v3)
    e4 = Edge(v3, 'r1', v4)

    g.add_edge(e1)
    g.add_edge(e2)
    g.add_edge(e3)
    g.add_edge(e4)

    g.commit()
    return g
