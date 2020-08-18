from Dev.GraphExamples.small_graphs import *
from Redis.config import Config
from Redis.server import RedisServer

config = Config("config.ini")

with RedisServer(config.redis_bin, config.redis_conf, verbose=False) as r:
    g = worstcase(r)
    res = g.query("""MATCH (a)-/ :A :B /->(b) RETURN a, b""")
    res.pretty_print()
