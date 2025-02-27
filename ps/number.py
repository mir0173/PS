#1056
from sys import stdin
input = stdin.readline
dp = {}

def f1(num, pows):
    if pows == 0:
        return 1
    k = f1(num, pows >> 1)
    return k * k if pows % 2 == 0 else num * k * k

def f2(num, k, trigger):
    m, M = 1, int(1e18)

    while m + 1 < M:
        mid = (m + M) >> 1
        m, M = (mid, M) if f1(mid, k) <= num else (m, mid)

    return m if trigger else M

def solve(index):
    if index == 1:
        return 0
    if index in dp:
        return dp[index]

    dp[index] = index - 1

    for i in range(1, 62):
        for trigger in (True, False):
            x = f2(index, i, trigger)
            if x >= index:
                continue
            dp[index] = min(dp[index], solve(x) + abs(index - f1(x, i)) + 1)

    return dp[index]

def main():
    n = int(input())
    print(solve(n))

if __name__ == '__main__':
    main()