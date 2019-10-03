
def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    print(graph)
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)



if __name__ == "__main__":
    # graph is in adjacent list representation
    graph = {
        '1': ['2', '3', '4'],
        '2': ['1', '5', '6'],
        '3': ['1'],
        '5': ['2', '9', '10'],
        '6': ['2'],
        '4': ['1', '7', '8'],
        '8': ['4'],
        '9': ['5'],
        '10': ['5'],
        '11': ['7'],
        '12': ['7'],
        '7': ['4', '11', '12']
    }

    print (bfs(graph, '1', '11'))