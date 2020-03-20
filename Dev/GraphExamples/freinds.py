from redisgraph import Graph, Node, Edge
from redis import Redis


def create_friends(r: Redis):
    g = Graph('friends', r)

    adam = Node(label='User', properties={'name': 'Adam', 'mail': 'fucker'})
    pernilla = Node(label='User', properties={'name': 'Pernilla'})
    david = Node(label='User', properties={'name': 'David'})

    g.add_node(adam)
    g.add_node(pernilla)
    g.add_node(david)

    g.add_edge(Edge(adam, 'FRIEND', pernilla))
    g.add_edge(Edge(pernilla, 'FRIEND', david))

    g.commit()
    return g
