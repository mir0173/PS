#1068
from sys import stdin
input = stdin.readline

n = int(input())
adj = [[] for _ in range(n)]
parents = list(map(int, input().split()))
root = 0
delete = int(input())

for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        if i != delete:
            adj[parents[i]].append(i)

if delete == root:
    print(0)
    exit(0)

ans = 0
def dfs(node: int):
    global ans

    if len(adj[node]) == 0:
        ans += 1
        return
    for n in adj[node]:
        dfs(n)

dfs(root)
print(ans)
