import heapq
def dijkstra(source,target,n,graph):
            priorityq = [(0, source)]
            dist = {i: float('inf') for i in range(n)}
            dist[source] = 0
            while priorityq:
                current, u = heapq.heappop(priorityq)
                
                if u == target:
                    return current
                
                if current > dist[u]:
                    continue
                
                for v, weight in graph[u]:
                    distance = current + weight
                    if distance < dist[v]:
                        dist[v] = distance
                        heapq.heappush(priorityq, (distance, v))
            return dist[target]
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(n)}
        for i in range(n - 1):
            graph[i].append((i + 1, 1))
        res= []
        for u, v in queries:
            graph[u].append((v, 1))
            short= dijkstra(0, n - 1,n,graph)
            res.append(short)
        return res
    