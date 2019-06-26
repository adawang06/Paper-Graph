import pandas as pd
from py2neo import Graph, Node, Relationship

edges = pd.read_csv("/Users/adawang/Desktop/df_matches_test.csv")
graph = Graph("bolt://ec2-54-200-13-63.us-west-2.compute.amazonaws.com:7687", auth=("neo4j", "wangda10"))

#for index, row in edges.iterrows():
#    graph.run('''
#      MATCH (a:id_A {property:$id_A))
#      MERGE (a)-[r:R_TYPE]->(b:id_B {property:$id_B))
#    ''', parameters = {'id_A': row['id_A'], 'id_B': row['id_B']})

for row in edges.iterrows():

    node_a = Node("paper_id", name = row[1]["id_A"])

    node_b = Node("paper_id", name = row[1]["id_B"])

    rel = Relationship(node_a, "is similar with", node_b)

    graph.merge(rel, "paper_id", "name")


#graph.delete_all()

print(edges.to_string())
