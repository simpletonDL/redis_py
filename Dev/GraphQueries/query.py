from typing import Callable

from Redis.config import Config
from Redis.server import *

from redis import Redis
from redisgraph import Graph

config = Config('config.ini')


def query(q, graph_factory: Callable[[Redis], Graph], run_query=False):
    r = start_redis_server(config.redis_bin, config.redis_conf)

    g = graph_factory(r)

    if run_query:
        result = g.query(q)
        print('Pretty answer:')
        result.pretty_print()
    else:
        print('Execution plan:')
        execution_plan = g.redis_con.execute_command('GRAPH.EXPLAIN', g.name, q)
        print('\n'.join([str(s.decode('utf-8')) for s in execution_plan]))

    stop_redis_server(6379)


def query_dev():
    r = start_redis_server(config.redis_bin, config.redis_conf)
    res = r.execute_command("graph.dev")
    print(res)
    stop_redis_server()

