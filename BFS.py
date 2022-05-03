graph={
    '1':['2','3'],
    '2':['4','5'],
    '3':['6'],
    '4':['7'],
    '5':['7'],
    '6':[],
    '7':[]
}
visited=[]
queue=[]
node='1'
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
        

bfs(visited,graph,node)

