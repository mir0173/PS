#1230
from sys import stdin
input = stdin.readline
INF = 1000

def main():
    a = input().rstrip()
    b = input().rstrip()
    na = len(a)
    nb = len(b)

    dp = [[[INF] * 2 for _ in range(nb + 1)] for _ in range(na + 1)]
    dp[0][0][0] = 0
    dp[0][0][1] = INF

    for i in range(1, nb + 1):
        dp[0][i][0] = INF
        dp[0][i][1] = 1

    for i in range(na):
        for j in range(i + 1):
            dp[i + 1][j][0] = dp[i + 1][j][1] = INF
        for j in range(i, nb):
            if a[i] == b[j]:
                dp[i + 1][j + 1][0] = min(dp[i][j][0], dp[i][j][1])
            else:
                dp[i + 1][j + 1][0] = INF
            dp[i + 1][j + 1][1] = min(dp[i + 1][j][0] + 1, dp[i + 1][j][1])

    r = min(dp[na][nb][0], dp[na][nb][1])
    print(-1 if r >= INF else r)

if __name__ == "__main__":
    main()