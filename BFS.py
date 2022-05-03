# BFS
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


def bfs(visited, graph, start_node, goal_node):
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        m = queue.pop(0)
        print(m)
        if m == goal_node:
            print("Node is Found !!! ")
            break;
        else:
            for n in graph[m]:
                if n not in visited:
                    visited.append(n)
                    queue.append(n)


print("The BFS Traversal is : ")

bfs(visited, graph, 'A', 'D')
