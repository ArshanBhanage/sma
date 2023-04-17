import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv("instagram.csv", nrows=100)
df = df.dropna()
print(df.head())

# Load edge list
# age and dob_year is my attribute ,you please add your dataset attributes
fb_graph = nx.from_pandas_edgelist(df, source="following", target="followers")
print(type(fb_graph))

# display all the nodes
print(list(fb_graph.nodes())[:10])

# display all the edges
print(list(fb_graph.edges())[:10])

# add new node in graph
fb_graph.add_edge("123.0", "2154.0")
print(fb_graph.nodes())

G = nx.Graph(fb_graph)

# display the facebook friends network
nx.draw(fb_graph, with_labels=True)
# plt.show()

# degree of each node
print(list(nx.degree(fb_graph))[:10])

print(nx.degree(fb_graph, 638.0))

# degree centrality
print(list(nx.degree_centrality(fb_graph))[:10])

sorted(nx.degree_centrality(fb_graph).values())
m_influential = nx.degree_centrality(G)
for w in sorted(m_influential, key=m_influential.get, reverse=True):
    print(w, m_influential[w])

pos = nx.spring_layout(G)
betCent = nx.betweenness_centrality(G, normalized=True, endpoints=True)
node_color = [20000.0 * G.degree(v) for v in G]
node_size = [v * 10000 for v in betCent.values()]
plt.figure(figsize=(20, 20))
nx.draw_networkx(G, pos=pos, with_labels=False, node_color=node_color, node_size=node_size)
print(sorted(betCent, key=betCent.get, reverse=True)[:5])
# plt.show()

# closeness centrality
closeness_centrality = nx.centrality.closeness_centrality(G)
print((sorted(closeness_centrality.items(), key=lambda item: item[1], reverse=True))[:8])

node_size = [v * 50 for v in closeness_centrality.values()]
plt.figure(figsize=(15, 8))
nx.draw_networkx(G, pos=pos, node_size=node_size, with_labels=False, width=0.15)
plt.axis("off")
# plt.show()

# bridges
print(nx.has_bridges(G))

bridges = list(nx.bridges(G))
print(len(bridges))

local_bridges = list(nx.local_bridges(G, with_span=False))
print(len(bridges))

plt.figure(figsize=(15, 5))
nx.draw_networkx(G, pos=pos, node_size=10, with_labels=False, width=0.15)
nx.draw_networkx_edges(G, pos, edgelist=local_bridges, width=0.5, edge_color="green")
nx.draw_networkx_edges(G, pos, edgelist=local_bridges, width=0.5, edge_color="blue")
plt.axis("off")
# plt.show()

# clustering
print(nx.average_clustering(G))
