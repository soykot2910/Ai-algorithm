graph = {
    1:[2,3],
    2:[4,5],
    3:[6],
    4:[],
    5:[6],
    6:[]

}

visited =[]

print("Depth limited search:")
def dfs(node,limit):
    if not limit: #if limit zero return zero
        return 0
    else:
        limit -=1
    if node not in visited:
        print (node,end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(neighbour,limit)

dfs(1,2)
