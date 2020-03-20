from redisgraph import Graph, Node, Edge
from redis import Redis


def create_simple(r: Redis):
    g = Graph('simple', r)

    v0 = Node(label='v0', properties={'name': 'v0'})
    v1 = Node(label='v1', properties={'name': 'v1'})
    v2 = Node(label='v2', properties={'name': 'v2'})
    v3 = Node(label='v3', properties={'name': 'v3'})
    v4 = Node(label='v4', properties={'name': 'v4'})

    g.add_node(v0)
    g.add_node(v1)
    g.add_node(v2)
    g.add_node(v3)
    g.add_node(v4)

    e1 = Edge(v0, 'r0', v1, properties={'name': 'r0'})
    e2 = Edge(v1, 'r1', v2, properties={'name': 'r1'})
    e3 = Edge(v2, 'r0', v3, properties={'name': 'r0'})
    e4 = Edge(v3, 'r1', v4, properties={'name': 'r1'})

    g.add_edge(e1)
    g.add_edge(e2)
    g.add_edge(e3)
    g.add_edge(e4)

    g.commit()
    return g


def create_simple_2(r: Redis):
    g = Graph('simple_2', r)

    v0 = Node(label='Man', properties={'name': 'v0'})
    v1 = Node(label='Man', properties={'name': 'v1'})
    v2 = Node(label='Woman', properties={'name': 'v2'})
    v3 = Node(label='Woman', properties={'name': 'v3'})
    v4 = Node(label='Woman', properties={'name': 'v4'})

    g.add_node(v0)
    g.add_node(v1)
    g.add_node(v2)
    g.add_node(v3)
    g.add_node(v4)

    e1 = Edge(v0, 'r0', v1, properties={'name': 'r0'})
    e2 = Edge(v1, 'r0', v2, properties={'name': 'r1'})
    e3 = Edge(v0, 'r0', v3, properties={'name': 'r0'})
    e4 = Edge(v3, 'r1', v2, properties={'name': 'r1'})
    e5 = Edge(v2, 'r1', v4, properties={'name': 'r1'})

    g.add_edge(e1)
    g.add_edge(e2)
    g.add_edge(e3)
    g.add_edge(e4)
    g.add_edge(e5)

    g.commit()
    return g


def worstcase(r: Redis):
    g = Graph('simple_2', r)

    v0 = Node(properties={'name': 'v0'})
    v1 = Node(properties={'name': 'v1'})
    v2 = Node(properties={'name': 'v2'})
    v3 = Node(properties={'name': 'v3'})
    v4 = Node(properties={'name': 'v4'})

    g.add_node(v0)
    g.add_node(v1)
    g.add_node(v2)
    g.add_node(v3)
    g.add_node(v4)

    e1 = Edge(v0, 'A', v1, properties={'name': 'r1'})
    e2 = Edge(v1, 'A', v2, properties={'name': 'r2'})
    e3 = Edge(v2, 'A', v0, properties={'name': 'r3'})
    e4 = Edge(v0, 'B', v3, properties={'name': 'r5'})
    e5 = Edge(v3, 'B', v0, properties={'name': 'r6'})

    g.add_edge(e1)
    g.add_edge(e2)
    g.add_edge(e3)
    g.add_edge(e4)
    g.add_edge(e5)

    g.commit()
    return g

