from sys import stdin
input = stdin.readline

x = input().strip()
y = input().strip()
adj = [[""] * (len(y) + 1) for _ in range(len(x) + 1)]
ans = []

def lcs(m, n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                adj[i][j] = adj[i - 1][j - 1] + x[i - 1]
            else:
                adj[i][j] = adj[i - 1][j] if len(adj[i - 1][j]) > len(adj[i][j - 1]) else adj[i][j - 1]
    return adj[m][n]

def main():
    p = lcs(len(x), len(y))
    print(len(p))
    if len(p) != 0:
        print(p)

if __name__ == '__main__':
    main()