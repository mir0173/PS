# 1211
from sys import stdin
input = stdin.readline

A, B = map(int, input().split())
ans = 0

def dfs(n, p):
    global ans
    if n != 0:
        f = n * p
        if A <= f <= B:
            ans += 1
    for d in range(1, 10):
        new_n = n * 10 + d
        new_p = p * d
        new_f = new_n * new_p
        if new_f > B:
            break
        dfs(new_n, new_p)

dfs(0, 1)
print(ans)

# 시간 초과 DP로 바꿀것

