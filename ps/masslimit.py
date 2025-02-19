import heapq
from sys import stdin
input = stdin.readline

def dijkstra(start, end, adj, dist):
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        ans, now = heapq.heappop(queue)
        ans *= -1

        if now == end:
            return ans

        if dist[now] <= ans:
            for List in adj[now]:
                if ans == 0: 
                    dist[List[1]] = List[0]
                    heapq.heappush(queue, (-dist[List[1]], List[1]))
                elif dist[List[1]] < List[0] and dist[List[1]] < ans:
                    dist[List[1]] = min(ans, List[0])
                    heapq.heappush(queue, (-dist[List[1]], List[1]))

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].append((c, b))
        adj[b].append((c, a))

    for i in range(1, n + 1):
        adj[i].sort(reverse=True)

    dist = [0 for _ in range(n + 1)]
    start, end = map(int, input().split())
    print(dijkstra(start, end, adj, dist))
    
if __name__ == "__main__":
    main()