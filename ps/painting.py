from sys import stdin
input = stdin.readline
from collections import defaultdict
N = int(input())
price = [list(map(int, input().rstrip())) for _ in range(N)]
dp = defaultdict(list)
dp[1] = [[0] * 10 for _ in range(N)]

def dfs(v, a, b):
    val = 0
    if not dp[v]:
        dp[v] = [[0] * 10 for _ in range(N)]

    if dp[v][a][b]:
        return dp[v][a][b]

    for i in range(N):
        if not (v & (1 << i)):
            if b <= price[a][i]:
                val = max(val, dfs(v | 1 << i, i, price[a][i]) + 1)
    dp[v][a][b] = val
    return val

def main():
    print(dfs(1, 0, 0) + 1)

if __name__ == '__main__':
    main()