N, M = map(int, input().split(" "))
# N: 島の数, M: 要望数
islands = []
# 西から[a_i, b_i]の配列
for _ in range(M):
  islands.append(list(map(int, input().split(" "))))

# counter = 0
# num_islands = len(islands)
# for i, m in enumerate(islands): 
#   a, b = islands[i][0], islands[i][1]
#   for j in range(i+1, num_islands):
#     c, d = islands[j][0], islands[j][1]
    
#     tmp = a * d - b * c
#     if tmp > 0:
#       counter += 1
# print(counter)

from collections import defaultdict
class SccGraph:
    def __init__(self, vertex_size):
        self.out_neighbour = defaultdict(list)
        self.vertex = set()
        self.visited = set()
        self.index = defaultdict(int)
        self.low_index = defaultdict(int)
        self.global_index = 0
        self.visit_stack = []
        self.scc = []
    def add_edge(self, from_node, to_node):
        self.vertex.add(from_node)
        self.vertex.add(to_node)
        self.out_neighbour[from_node].append(to_node)
    def dfs_graph(self):
        for v in self.vertex:
            if v not in self.visited:
                self.dfs_node(v)
    def dfs_node(self, v):
        # for safe protection
        if v in self.visited:
            return
        self.index[v] = self.global_index
        self.low_index[v] = self.global_index
        self.global_index += 1
        self.visit_stack.append(v)
        self.visited.add(v)
        for n in self.out_neighbour[v]:
            if n not in self.visited:
                self.dfs_node(n)
                self.low_index[v] = min(self.low_index[v], self.low_index[n])
            elif n in self.visit_stack:
                self.low_index[v] = min(self.low_index[v], self.index[n])
        result = []
        if self.low_index[v] == self.index[v]:
            w = self.visit_stack.pop(-1)
            while w != v:
                result.append(w)
                w = self.visit_stack.pop(-1)
            result.append(v)
            self.scc.append(result)


g = SccGraph(M)
# setup a graph 1->2->3 and 3 -> 1 which forms a scc
# setup another two edges 3->4 and 4->5
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,1)
g.add_edge(3,4)
g.add_edge(4,5)
g.dfs_graph()
print(g.scc)