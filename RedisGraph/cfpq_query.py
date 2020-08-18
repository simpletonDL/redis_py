from redisgraph import Graph


class CfpqResponse:
    def __init__(self, resp):
        self.time = float(resp[0][1].decode('utf-8'))
        self.iters = int(resp[1][1])
        self.control_sums = {
            key.decode('utf-8'): value
            for key, value in resp[2]
        }

        self.index_time = None
        self.paths_stat = []
        if len(resp) == 4:
            self.index_time = float(resp[3].decode('utf-8'))
            # self.paths_stat = [[left, right, length, float(time.decode('utf-8'))]
            #                    for left, right, length, time in resp[3][1]]

    def __str__(self):
        return f'Time: {self.time}\n' \
               f'Iters: {self.iters}\n' \
               f'Control sum: {self.control_sums}\n' \
               f'Index time: {self.index_time} \n'
        #      f'Path stat: {sorted(Counter([xs[2] for xs in self.paths_stat]).items())}'


class GraphCfpq(Graph):
    def __init__(self, name, redis_con):
        super().__init__(name, redis_con)

    def cfpq_query(self, algo, grammar_path):
        """
        Executes a query against the graph.
        """

        response = self.redis_con.execute_command("GRAPH.CFG", algo, self.name, grammar_path)
        return CfpqResponse(response)
