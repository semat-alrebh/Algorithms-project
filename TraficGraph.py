import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# ---------------------------------------------------
# STEP 1: Read the dataset
# Make sure roadNet-CA.txt is in the same folder as this file
# ---------------------------------------------------
df = pd.read_csv('roadNet-CA.txt', sep='\t', comment='#',
                 names=['from', 'to'])

# ---------------------------------------------------
# STEP 2: Clean the data
# ---------------------------------------------------
df = df.dropna()                     # Remove missing values
df = df.drop_duplicates()            # Remove duplicate roads
df = df[df['from'] != df['to']]      # Remove self-loops

print("Total roads (edges):", len(df))
print(df.head(10))

# ---------------------------------------------------
# STEP 3: Convert to Graph
# ---------------------------------------------------
G = nx.from_pandas_edgelist(df, 'from', 'to')

print("Total intersections (nodes):", G.number_of_nodes())
print("Total roads (edges):", G.number_of_edges())

# ---------------------------------------------------
# STEP 4: Draw a small sample of the Graph (first 500 nodes)
# ---------------------------------------------------
small = G.subgraph(list(G.nodes())[:500])

plt.figure(figsize=(10, 8))
nx.draw(small, node_size=5, edge_color='gray', node_color='blue', alpha=0.6)
plt.title("Road Network Graph - Sample (500 nodes)")
plt.savefig('graph_screenshot.png', dpi=150)
plt.show()

print("Graph image saved as graph_screenshot.png")
