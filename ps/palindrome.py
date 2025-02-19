from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    m = list(input().rstrip())
    n2 = m[::-1]
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) if m[i - 1] != n2[j - 1] else dp[i-1][j-1] + 1
    print(n - dp[-1][-1])

if __name__ == '__main__':
    main()