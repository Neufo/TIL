small = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D', 'F'],
    'F': ['E'],
}


def degreesOfSeparation(graph, start, end):
    if len(graph) == 0:
        return 0

    flontier = {start}
    visited = {start}
    degrees = 0

    flontiers = [flontier]

    while len(flontier) > 0:
        print('degrees', ':', str(degrees))
        print(flontier)
        degrees += 1

        new_flontier = set()
        for v in flontier:
            for nv in graph[v]:
                if nv not in visited:
                    visited.add(nv)
                    new_flontier.add(nv)
        if end in new_flontier:
            flontier = {end}
        else:
            flontier = new_flontier
        flontiers.append(flontier)

    route = [end]
    current = end
    for i in range(len(flontiers)-2, -1, -1):
        previous = flontiers[i]
        for v in previous:
            if current in graph[v]:
                current = v
                route.append(v)
                break

    route.reverse()
    return degrees-1, route


degree, route = degreesOfSeparation(small, 'A', 'F')
print(degree)
print(route)
