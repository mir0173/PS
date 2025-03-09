#1043
from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    s = set(input().split()[1:])
    l = []
    for _ in range(m):
        l.append(set(input().split()[1:]))

    for _ in range(m):
        for party in l:
            s |= party if party & s else s

    ans = 0
    for party in l:
        ans += 0 if party & s else 1

    print(ans)

if __name__ == '__main__':
    main()