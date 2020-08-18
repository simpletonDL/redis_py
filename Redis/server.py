import os
import subprocess
import sys
import time
from shutil import copyfile

import redis


class RedisServer:
    def __init__(self, redis_bin, redis_conf='redis.conf', port=6379, dump=None, verbose=False):
        self.redis_bin = redis_bin
        self.redis_conf = redis_conf
        self.port = port
        self.dump = dump
        self.verbose = verbose

    def __enter__(self):
        return self.start_redis_server()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_redis_server()

    def start_redis_server(self):
        if self.dump:
            copyfile(self.dump, 'dump.rdb')

        cmd = [self.redis_bin, self.redis_conf, '--port', str(self.port)]
        with open(os.devnull) as devnull:
            subprocess.Popen(cmd, stdout=sys.stdout if self.verbose else devnull)

        r = redis.Redis(port=self.port)
        while True:
            try:
                if r.ping():
                    break
            except redis.exceptions.RedisError:
                time.sleep(0.5)
                pass
        return r

    def stop_redis_server(self):
        redis.Redis(port=self.port).shutdown(True)
        if os.path.exists('dump.rdb'):
            os.remove('dump.rdb')
