import os
from typing import List
from Redis.config import Config

SUIT_TO_GRAMMARS = {
    'SG_1': ['SG.yrd'],
    'SG_2': ['SG.yrd'],
    'FreeScale': ['an_bm_cm_dn.txt'],
    'FullGraph': ['A_star0.yrd', 'A_star1.yrd', 'A_star2.yrd'],
    'RDF': ['GPPerf1_cnf.txt'],  # 'GPPerf2_cnf.txt'],  # , 'geo.cnf'],
    'MemoryAliases': ['mayAlias.yrd'],
    'WorstCase': ['Brackets.txt'],
    'Geo': ['geo.cnf']
}


def _get_suits_root(cfpq_data_path: str):
    return os.path.join(cfpq_data_path, 'data', 'graphs')


def _get_suit_path(cfpq_data_path: str, suite: str):
    return os.path.join(_get_suits_root(cfpq_data_path), suite)


def _get_matrices_path(cfpq_data_path: str, suite: str):
    return os.path.join(_get_suit_path(cfpq_data_path, suite), 'Matrices')


def get_grammar_path(cfpq_data_path: str, suite: str, grammar: str):
    return os.path.join(_get_suit_path(cfpq_data_path, suite), 'Grammars', grammar)


def get_rdb_graph(conf: Config, graph: str):
    return os.path.join(conf.redis_dumps_path, graph.replace('.txt', '.rdb'))


def get_suites(conf: Config):
    return os.listdir(_get_suits_root(conf.cfpq_data_path))


def get_graph_cases(conf: Config):
    g_test_suits = {}
    for suite in get_suites(conf):
        g_test_suits[suite] = [g for g in os.listdir(_get_matrices_path(conf.cfpq_data_path, suite))
                               if not g.startswith('.')]
    return g_test_suits


def get_additional_cases(conf: Config):
    return [
        ('geospeices.txt', get_grammar_path(conf.cfpq_data_path, 'RDF', 'geo.cnf'))
    ]


def get_suits_cases(suits: List[str], conf: Config):
    graph_cases = get_graph_cases(conf)
    grammar_cases = SUIT_TO_GRAMMARS

    return sum([
        sorted([(graph_case, get_grammar_path(conf.cfpq_data_path, suite, grammar_case))
                for graph_case in graph_cases[suite]
                for grammar_case in grammar_cases[suite]],
               key=lambda case: (case[1], case[0]))
        for suite in suits], [])


def get_total_cases(conf: Config):
    return get_additional_cases(conf) + get_suits_cases(get_suites(conf), conf)
