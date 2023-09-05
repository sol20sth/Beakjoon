import heapq
import sys
input = sys.stdin.readline

INF = float("INF")

def dijkstra():
    heap = []
    heapq.heappush(heap,(0,0))
    distance[0] = 0
    while heap:
        dist, now = heapq.heappop(heap)
        if dist > distance[now]:
            continue
        # print(now, heap)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap,(cost, i[0]))

n , d = map(int,input().split())
graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

for i in range(d):
    graph[i].append((i+1, 1))
# print(graph)
for _ in range(n):
    s, e, l = map(int,input().split())
    if e > d:
        continue
    graph[s].append((e,l))

dijkstra()
print(distance[d])