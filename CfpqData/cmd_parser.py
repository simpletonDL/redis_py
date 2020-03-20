from argparse import ArgumentParser
from itertools import chain

from CfpqData.test_suits import *


def get_cmd_parser(conf: Config):
    parser = ArgumentParser('Load rdf into RedisGraph')

    # parser.add_argument('--host', help='redis host name', default='localhost')
    parser.add_argument('--port', help='redis port', default=6379)

    subparsers = parser.add_subparsers()

    parser_graph = subparsers.add_parser('graph')
    parser_graph.add_argument('suite', help='suite name', choices=get_suites(conf))
    parser_graph.add_argument('graph', help='graph name', choices=list(chain(*get_graph_cases(conf).values())))

    parser_suite = subparsers.add_parser('suite')
    parser_suite.add_argument('-s', action='append', choices=get_suites(conf), required=True)

    return parser
