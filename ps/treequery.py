#15681
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)


def dfs(now, m, visit):
    visit[now] = 1
    for i in m[now]:
        if visit[i] == -1: 
            visit[now] += dfs(i, m, visit) 
    return visit[now] 

def main():
    n, r, q = map(int, input().split())
    m=[[]for _ in range(n + 1)]
    visit=[-1 for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        m[a].append(b)
        m[b].append(a)
    dfs(r, m, visit)
        
    for _ in range(q):
        query = int(input())
        print(visit[query])

if __name__ == '__main__':
    main()