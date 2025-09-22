class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False

def get_edges(graph):
    edges = []
    seen = set()
    for u in graph:
        for v, w in graph[u]:
            if (v, u) not in seen:  
                edges.append((w, u, v))
                seen.add((u, v))
    return edges

def kruskal_mst(graph):
    edges = get_edges(graph)
    edges.sort()
    ds = DisjointSet(graph.keys())
    mst = []
    for weight, u, v in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
    return mst

graph = {
    'A': [('B', 9), ('C', 4)],
    'B': [('C', 2), ('E', 7), ('A', 9), ('D', 1)],
    'C': [('D', 4), ('A', 4), ('B', 2), ('F', 3)],
    'D': [('B', 1), ('E', 2), ('F', 5), ('C', 4)],
    'E': [('B', 7), ('D', 2), ('F', 6), ('G', 3)],
    'F': [('D', 5), ('E', 6), ('G', 8), ('H', 5)],
    'G': [('E', 3), ('F', 8), ('H', 1), ('I', 3)],
    'H': [('F', 5), ('G', 1), ('I', 2)],
    'I': [('G', 3), ('H', 2)]
}

mst = kruskal_mst(graph)

print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} - {v}: {w}")
                                              
