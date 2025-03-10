#1099
from sys import stdin
input = stdin.readline

def check(a, b, l):
    tmp = 0
    for i in range(l):
        if a[i] != b[i]:
            tmp += 1
    return tmp

def main():
    s = " "+input().strip()
    n = int(input())
    words = [input().strip() for _ in range(n)]
    dp = [[1000] * (len(s)) for _ in range(len(s))]
    dp[0][0] = 0

    for i in range(1, len(s) + 1):
        if dp[i - 1][0] == 1000: continue
        for word in words:
            l = len(word)
            if sorted(s[i:i + l]) == sorted(word):
                dp[i][i + l - 1] = min(dp[i][i + l - 1], dp[i - 1][0] + check(s[i:i + l], word, l))
                dp[i + l - 1][0] = min(dp[i + l - 1][0],dp[i][i + l - 1])

    print(dp[-1][0] if dp[-1][0] != 1000 else -1)

if __name__ == '__main__':
    main()