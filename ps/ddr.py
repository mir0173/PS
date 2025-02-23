#2342
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def cost(a, b): 
    if b == 0:
        return 0 if a == 0 else 2
    elif b == a:
        return 1
    elif abs(b - a) == 1 or abs(b - a) == 3:
        return 3
    else:
        return 4

def main():
    move = list(map(int, input().split()))
    move.pop()
    n = len(move)
    if n == 0:
        print(0)
        return

    dp = [[[4e5 + 1 for _ in range(5)] for _ in range(5)] for _ in range(n + 1)]
    dp[-1][0][0] = 0

    for i in range(n):
        for j in range(5):
            for k in range(5):
                add = cost(move[i], k)
                dp[i][move[i]][j] = min(dp[i][move[i]][j], dp[i - 1][k][j] + add)

        for l in range(5):
            for m in range(5):
                add = cost(move[i], m)
                dp[i][l][move[i]] = min(dp[i][l][move[i]], dp[i - 1][l][m] + add)

    m = 4e5 + 1
    for i in range(5):
        for j in range(5):
            m = min(m, dp[n - 1][i][j])
    print(m)

if __name__ == '__main__':
    main()