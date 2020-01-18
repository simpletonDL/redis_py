import os
import time
from shutil import copyfile

import redis


def start_redis_server(bin_path, redis_conf_path, dump_path=None, port=6379):
    if dump_path:
        copyfile(dump_path, 'dump.rdb')

    os.spawnvpe(os.P_NOWAIT, bin_path, [bin_path, redis_conf_path, '--port', str(port)], os.environ)

    r = redis.Redis(port=port)
    while True:
        try:
            if r.ping():
                break
        except redis.exceptions.RedisError as e:
            time.sleep(0.5)
            pass
    print('Redis has started')
    return r


def stop_redis_server(port=6379):
    redis.Redis(port=port).shutdown(True)
    if os.path.exists('dump.rdb'):
        os.remove('dump.rdb')
    print('Redis has stop')
