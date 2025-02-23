#9466
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))

def dfs(x, ans):
    visit[x] = True
    cycle.append(x)  
    num = nums[x]

    if visit[num]:  
        if num in cycle: 
            ans += cycle[cycle.index(num):] 
        return
    else:
        dfs(num, ans)


for _ in range(int(input())):
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    visit = [True] + [False] * n 
    ans = []

    for i in range(1, n + 1):
        if not visit[i]:  
            cycle = []
            dfs(i, ans) 

    print(n - len(ans))  
