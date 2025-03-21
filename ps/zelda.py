#4485
import heapq
from sys import stdin
input = stdin.readline
INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(n, adj, d, key):
    q = []
    heapq.heappush(q, (adj[0][0], 0, 0))
    d[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n - 1 and y == n - 1:
            print(f'Problem {key}: {d[x][y]}')
            break

        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]

            if 0 <= new_x < n and 0 <= new_y < n:
                new_cost = cost + adj[new_x][new_y]

                if new_cost < d[new_x][new_y]:
                    d[new_x][new_y] = new_cost
                    heapq.heappush(q, (new_cost, new_x, new_y))

def main():
    key = 1
    while True:
        n = int(input())
        if n == 0: break
        adj = [list(map(int, input().split())) for _ in range(n)]
        d = [[INF] * n for _ in range(n)]
        dijkstra(n, adj, d, key)
        key += 1

if __name__ == '__main__':
    main( )