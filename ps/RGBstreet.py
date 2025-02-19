#17404
from sys import stdin
input = stdin.readline

max = 1e6
r, g, b = 0, 1, 2

def main():
    N = int(input())
    cost = [[-1, -1, -1]]
    for _ in range(N):
        cost.append(list(map(int, input().split())))

    answer = max
    for rgb in [r,g,b]:
        dp = [[-1, -1, -1] for _ in range(N+1)]

        dp[1] = [max, max, max]
        dp[1][rgb] = cost[1][rgb]

        for i in range(2, N + 1):
            dp[i][r] = min(dp[i - 1][g], dp[i - 1][b]) + cost[i][r]
            dp[i][g] = min(dp[i - 1][r], dp[i - 1][b]) + cost[i][g]
            dp[i][b] = min(dp[i - 1][r], dp[i - 1][g]) + cost[i][b]
        dp[N][rgb] = max
        answer = min(answer, min(dp[N]))
    print(answer)

if __name__ == '__main__':
    main()