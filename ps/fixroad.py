#15670
from sys import stdin
input = stdin.readline

def main():
    ans = []
    n, m = map(int, input().split())
    a = [int(2e9)] + list(map(int, input().split())) + [0] * (n + 1)
    up, dn = [0] * (n + 2), [0] * (n + 2)
    up[1] = dn[1] = 1

    for i in range(2, n + 1):
        up[i] = up[i - 1]
        dn[i] = dn[i - 1]
        if a[i] > a[i - 1]: dn[i] += 1
        else: up[i] += 1

    for _ in range(m):
        l, r = map(int, input().split())
        v = up[l - 1] + up[n] - up[r] + dn[r] - dn[l - 1]
        if up[r] == up[r + 1]: v += 1
        if dn[l] == dn[l - 1]: v += 1
        if a[r] > a[l - 1]: v -= 1
        if a[l] < a[r + 1]: v -= 1
        ans.append(str(v))
    print(*ans, sep = "\n")

if __name__ == "__main__":
    main()
