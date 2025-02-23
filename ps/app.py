#7579
from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    list1 = [0] + [int(x) for x in input().split()]
    list2 = [0] + [int(x) for x in input().split()]
    dp = [[0] * (sum(list2) + 1) for _ in range(n + 1)]
    ans = sum(list2)

    for i in range(1, n + 1):
        for j in range(sum(list2) + 1):
            dp[i][j] = dp[i - 1][j]
        for j in range(list2[i], sum(list2) + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - list2[i]] + list1[i])
            if dp[i][j] >= m:
                ans = min(ans, j)

    print(ans)

if __name__ == '__main__':
    main()