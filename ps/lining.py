# 2252
from sys import stdin
input = stdin.readline
from collections import deque

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    list = [0 for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        list[b] += 1
    
    queue = deque()
    for i in range(n):
        if list[i + 1] == 0:
            queue.append(i + 1)
    
    while queue:
        tmp = queue.popleft()
        for j in adj[tmp]:
            list[j] -= 1
            if list[j] == 0:
                queue.append(j)
        print(tmp, end=" ")
        
if __name__ == '__main__':
    main()