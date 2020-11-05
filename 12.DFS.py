
graph = {
    1:[2,3,4],
    2:[],
    3:[5],
    4:[6],
    5:[],
    6:[]

}

visited =[]

print("Depth first search:")

def dfs(node):
    if node not in visited:
        print (node,end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(neighbour)

dfs(1)
