from shutil import move

from CfpqData.cmd_parser import *
from Redis.config import Config
from Redis.server import *
from RedisGraph.cfpq_query import *
import numpy as np
import pandas as pd

conf = Config('config.ini')
parser = get_cmd_parser(conf)
args = parser.parse_args()


def file_len(f):
    with open(f) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def projection(i):
    return lambda x: x[i]


def exec_on_graph(suite, graph, grammar, conf, verbose=True):
    grammar_path = get_grammar_path(conf.cfpq_data_path, suite, grammar)
    dump_path = get_rdb_graph(conf, graph)

    r = start_redis_server(conf.redis_bin, conf.redis_conf, dump_path=dump_path, port=args.port)
    g = GraphCfpq(graph, r)
    if verbose:
        print(f'Graph: {graph}, Grammar: {grammar}')
    resp = g.cfpq_query('cpu4', grammar_path)

    stop_redis_server()
    return resp


def response_to_df(resp: CfpqResponse, graph: str, grammar: str):
    path_stat = pd.DataFrame({
        'graph': graph,
        'grammar': grammar,
        'i': list(map(projection(0), resp.paths_stat))[:5],
        'j': list(map(projection(1), resp.paths_stat))[:5],
        'length': list(map(projection(2), resp.paths_stat))[:5],
        'time': list(map(projection(3), resp.paths_stat))[:5],
    })

    hist, bins = np.histogram(list(map(projection(2), resp.paths_stat)), 5)
    bins = list(map(int, bins))

    index_stat = pd.DataFrame({
        'graph': graph,
        'grammar': grammar,
        'constrol_sum': str(resp.control_sums),
        'total_time': resp.time,
        'index_time': resp.index_time,
        'path_stat': [str(hist.ravel())],
        'stat_ranges': [str(bins)]
    })

    return path_stat, index_stat


if 'graph' in args:
    suites = [args.suite]
else:
    suites = args.s

path_stat_dir = os.path.join('results', 'path_stat')
for d in ['results', path_stat_dir]:
    if not os.path.exists(d):
        os.mkdir(d)

for suite in suites:
    suite_dir = os.path.join(path_stat_dir, suite)
    if not os.path.exists(suite_dir):
        os.mkdir(suite_dir)

    for grammar in SUIT_TO_GRAMMARS[suite]:
        grammar_dir = os.path.join(suite_dir, grammar)
        if not os.path.exists(grammar_dir):
            os.mkdir(grammar_dir)

        for graph in get_graph_cases(conf)[suite]:
            resp = exec_on_graph(suite, graph, grammar, conf)
            graph_file = f'{graph}.csv'
            move(graph_file, os.path.join(grammar_dir, graph_file))

            time_info_file = os.path.join('results', 'time_info.csv')
            header = not os.path.exists(time_info_file)
            with open(time_info_file, 'a') as f:
                time_info_df = pd.DataFrame({
                    'graph': [graph],
                    'grammar': grammar,
                    'constrol_sum': str(resp.control_sums),
                    'total_time': resp.time,
                    'index_time': resp.index_time,
                })
                print(graph, grammar, resp.control_sums, resp.time, resp.index_time)
                time_info_df.to_csv(f, header=header, index=False)
