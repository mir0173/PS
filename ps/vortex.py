from sys import stdin
input = stdin.readline

def main():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    r1, c1, r2, c2 = map(int, input().split())
    adj = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
    tot = (r2 - r1 + 1) * (c2 - c1 + 1)
    key, d, n, x, y, m = 1, 1, 1, 0, 0, 0
    
    while tot > 0:
        for _ in range(2):
            for _ in range(n):
                if r1 <= x <= r2 and c1 <= y <= c2:
                    adj[x - r1][y - c1] = key
                    tot -= 1
                    m = key
                x += dx[d]
                y += dy[d]
                key += 1
            d = (d - 1) % 4
        n += 1
    
    m_len = len(str(m))
    for i in range(r2 - r1 + 1):
        for j in range(c2 - c1 + 1):
            print(str(adj[i][j]).rjust(m_len), end=" ")
        print()

if __name__ == '__main__':
    main()