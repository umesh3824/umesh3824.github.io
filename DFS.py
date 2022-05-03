# DFS
graph = {'A': ['B', 'E', 'C'],
         'B': ['A', 'D', 'E'],
         'D': ['B', 'E'],
         'E': ['A', 'D', 'B'],
         'C': ['A', 'F', 'G'],
         'F': ['C'],
         'G': ['C']
         }

visited = []
queue = []


def dfs(visited, graph, g):
    if g not in visited:
        print(g)
        visited.append(g)
        # queue.append(m)
        for n in graph[g]:
            dfs(visited, graph, n)


dfs(visited, graph, 'A')
