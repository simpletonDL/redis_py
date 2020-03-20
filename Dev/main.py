from collections import Counter
from functools import reduce

from Dev.GraphExamples.small_graphs import *
from Dev.GraphExamples.freinds import *
from Dev.GraphQueries.query import *

# query("MATCH (a:v0)-[r_0:r0]->(b:v1)-[r_1:r1]->(c:v2), (d)-[]->(e) RETURN a,b,c,r_0,r_1", create_simple)
# query("MATCH (a:v0)-[r_0:r0]->(b:v1)-[r*]->(c:v3)-[r_1:r1]->(d:v4) RETURN a, b, c", create_simple, True)
# query("MATCH (a)-[e1:r1]->(b)<-[e2:r2]->(c), (b)<-[e3:r3]-(d), (a)-[e4:r4]->(e) RETURN a, b", create_simple_2, False)

# FIRST EXAMPLE
# query("MATCH (a)-[e1:r1*]->(b:l3)<-[e2:r2]-(c:l2)<-[e3:r3]-(d:l1) RETURN 5", create_simple_2, False)

# SECOND EXAMPLE
# query("MATCH (a:la)-[e1:r1]->()<-[e2:r2]-(c),"
#       "(c)-[]->(d)-[]->(e:le),"
#       "(e:le)-[e3:r3*]->(f:lf),"
#       "(f:lf)-[e4 :r4 | :r5 | :r6]->(g:lg)"
#       "RETURN c", create_simple_2, False)

# CRUSHED EXAMPLE
# query("MATCH ()-[e1]-()-[e2]-() RETURN 5", create_simple_2, False)

# THIRD EXAMPLE
# query("MATCH (a)-[:r1]->(b:B)-[:PATTERN]->(c:C)-[:r3]->(d) RETURN 5", create_simple_2, False)

# query("MATCH (:A)-[r]->(:B)-[:PATTERN]->(:C) RETURN r", create_simple_2, False)
# stop_redis_server()
# query("MATCH (a)-[:PATTERN]->(c) RETURN a.name, c.name", worstcase, True)


fin = open("input.txt", "r")

text = fin.read()
text = "".join([x if x.isalpha() or x == '\n' else ' ' for x in text])

lines = text.split('\n')
words = [x for line in lines for x in line.split()]
letters = [x for x in text if x != ' ']
print(len(lines), len(words), len(letters))

# query_dev()
