#9029
from sys import stdin
input = stdin.readline
inf = float('inf')
num = 201

def main():
    dp = [[[inf] * num for _ in range(num)] for _ in range(num)]
    ans = []
    for i in range(1, num):
        for j in range(1, num):
            for k in range(1, num):
                if dp[i][j][k] < inf: continue
                if i == j == k: dp[i][j][k] = 1
                elif i % k == j % k == 0: dp[i][j][k] = (i // k) * (j // k)
                elif i % j == k % j == 0: dp[i][j][k] = (i // j) * (k // j)
                elif j % i == k % i == 0: dp[i][j][k] = (j // i) * (k // i)
                else:
                    for l in range(1, max(i, j, k) // 2 + 1):
                        if l <= i // 2: dp[i][j][k] = min(dp[i][j][k], dp[l][j][k] + dp[i - l][j][k])
                        if l <= j // 2: dp[i][j][k] = min(dp[i][j][k], dp[i][l][k] + dp[i][j - l][k])
                        if l <= k // 2: dp[i][j][k] = min(dp[i][j][k], dp[i][j][l] + dp[i][j][k - l])
                for a, b, c in [(i, j, k), (i, k, j), (j, i, k), (j, k, i), (k, j, i), (k, i, j)]: dp[a][b][c] = dp[i][j][k]

    def solve():
        w, l, h = map(int, input().split())
        ans.append(dp[w][l][h])

    for _ in range(int(input())): solve()
    print(*ans, sep = "\n")

if __name__ == '__main__':
    main()