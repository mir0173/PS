#1053
from sys import stdin
input = stdin.readline

def factory(left, right):
    if dp[left][right] != -1:  return dp[left][right]
    if left >= right:  return 0
    dp[left][right] = min(factory(left + 1, right) + 1, factory(left, right - 1) + 1, factory(left + 1, right - 1) + (n[left] != n[right]))
    return dp[left][right]

def main():
    global n, dp
    n = list(input().rstrip())
    dp = [[-1] * len(n) for _ in range(len(n))]
    ans = factory(0, len(n) - 1)
    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            n[i], n[j] = n[j], n[i]
            dp = [[-1] * len(n) for _ in range(len(n))]
            ans = min(ans, factory(0, len(n) - 1) + 1)
            n[i], n[j] = n[j], n[i]
    print(ans)

if __name__ == '__main__':
    main()