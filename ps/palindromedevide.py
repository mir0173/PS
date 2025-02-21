#1509
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
n = input().rstrip()
m = len(n)
dp = [2500 for _ in range(m + 1)]
dp[-1] = 0
pelin = [[0 for j in range(m)] for i in range(m)]

def main():
    for i in range(m):
        pelin[i][i] = 1

    for i in range(1, m):
        if n[i - 1] == n[i]:
            pelin[i - 1][i] = 1

    for i in range(3, m + 1):
        for j in range(m - i + 1):
            if n[j] == n[j + i - 1] and pelin[j + 1][j + i - 2]:
                pelin[j][j + i - 1] = 1

    for end in range(m):
        for start in range(end + 1):
            dp[end] = min(dp[end], dp[start - 1] + 1) if pelin[start][end] else min(dp[end], dp[end - 1] + 1)

    print(dp[m - 1] - 1)

if __name__ == '__main__':
    main()