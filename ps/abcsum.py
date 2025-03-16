#1132
from sys import stdin
input = stdin.readline
n = int(input())
adj = [[0, False] for _ in range(10)]

def main():
    ans = 0
    for _ in range(n):
        s = [ord(c) - 65 for c in input().rstrip()]
        tmp = 1
        adj[s[0]][1] = True

        for c in range(len(s) - 1, -1, -1):
            adj[s[c]][0] += tmp
            tmp *= 10
    adj.sort(reverse = True)

    if adj[9][1]:
        for i in range(8, -1, -1):
            if not adj[i][1]:
                del adj[i]
                break

    for i in range(9):
        ans += adj[i][0] * (9 - i)
    print(ans)

if __name__ == '__main__':
    main()