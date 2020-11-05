graph = {
    1:[2,3,4],
    2:[],
    3:[5],
    4:[6],
    5:[],
    6:[]

}
visited = []
queue = []

def bfs( node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print (s, end = " ")

        for neighbour in graph:
             if neighbour not in visited:#neighbour group ar modde ase kina
                visited.append(neighbour)
                queue.append(neighbour)

bfs(1)
