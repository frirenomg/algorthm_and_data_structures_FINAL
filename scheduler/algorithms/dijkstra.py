import heapq

def dijkstra(graph, start):
    if start not in graph:
        return {}

    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for to, w in graph[v]:
            if dist[to] > d + w:
                dist[to] = d + w
                heapq.heappush(pq, (dist[to], to))
    return dist
