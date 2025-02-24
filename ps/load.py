#1045
from sys import stdin
input = stdin.readline
import heapq

n, m = map(int, input().split())
map = [list(input().strip()) for _ in range(n)]
pqlist = []
nolist = list() 
list = [*range(n)]
ans = [0] * n

def f(x):
    while x != list[x]:
        x = list[x]
    return x


def union(x, y):
    px = f(x)
    while y != list[y]:
        temp, y = y, list[y]
        list[temp] = px
    list[y] = px


def main():
    pqlist = []
    for i in range(n):
        for j in range(i, n):
            if map[i][j] == 'Y':
                heapq.heappush(pqlist, (i, j))      

    if len(pqlist) < m:     
        print(-1)
        return

    cnt = 0
    while pqlist:
        i, j = heapq.heappop(pqlist)
        if f(i) != f(j):
            union(i, j)
            ans[i] += 1     
            ans[j] += 1
            cnt += 1
        else:
            heapq.heappush(nolist, (i, j))     

    if cnt != n - 1:       
        print(-1)
        return

    for _ in range(m - cnt):
        i, j = heapq.heappop(nolist)
        ans[i] += 1
        ans[j] += 1

    print(*ans)

if __name__ == '__main__':
    main()