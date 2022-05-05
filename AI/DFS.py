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
stack=[]
node='1'
def dfs(visited,graph,node):
    visited.append(node)
    stack.insert(0,node)
    while stack:
        m=stack.pop(0)
        print(m)
        l=graph[m]
        l.reverse()
        for neighbour in l:
            if neighbour not in visited:
                stack.insert(0,neighbour)
                visited.append(neighbour)
        

dfs(visited,graph,node)

