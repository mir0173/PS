#11049
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    adj = [tuple(map(int, input().split())) for i in range(n)]

    dp = [[0] * n for i in range(n)]
    for key in range(n - 1):
        for i in range(n - 1 - key):
            m, dp[i][m] = i + key + 1, 1e9
            for j in range(i, m):
                dp[i][m] = min(dp[i][m], dp[i][j] + dp[j + 1][m] + adj[i][0] * adj[j][1] * adj[m][1])
    print(dp[0][-1])

if __name__ == '__main__':
    main()