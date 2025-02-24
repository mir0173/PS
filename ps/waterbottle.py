from sys import stdin
input = stdin.readline

def main():
    n, k = map(int, input().split())
    ans = 0
    while bin(n).count('1') > k:
        idx = list(reversed(bin(n))).index('1')
        ans, n = ans + 2 ** idx, n + 2 ** idx
    print(ans)

if __name__ == '__main__':
    main()