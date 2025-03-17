#1082
import math
from sys import stdin
input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
dp = [-math.inf for _ in range(m + 1)]
for i in range(n - 1, -1, -1):
    tmp = arr[i]
    for j in range(tmp, m + 1):
        dp[j] = max(dp[j - tmp] * 10 + i, i, dp[j])

print(dp[m])
