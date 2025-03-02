#1047
from sys import stdin
input = stdin.readline

class Fen:
    def __init__(self, y, x, z, n):
        self.y = y
        self.x = x
        self.z = z
        self.n = n

def main():
    n = int(input())
    fen, x_fen, y_fen = [], [], []

    for _ in range(n):
        y, x, z = map(int, input().split())
        fen.append(Fen(y, x, z, 0))

    fen.sort(key=lambda a: a.z, reverse=True)

    for i in range(n):
        fen[i].n = i

    x_fen = fen[:]
    y_fen = fen[:]
    x_fen.sort(key=lambda a: a.x)
    y_fen.sort(key=lambda a: a.y)

    ans = 100000

    for r in range(n - 1, -1, -1):
        for l in range(0, r + 1):
            for u in range(n - 1, -1, -1):
                for d in range(0, u + 1):
                    leng = 0
                    key = 0
                    memo = [False] * n

                    for i in range(r + 1, n):
                        memo[y_fen[i].n] = True
                    for i in range(l - 1, -1, -1):
                        memo[y_fen[i].n] = True
                    for i in range(u + 1, n):
                        memo[x_fen[i].n] = True
                    for i in range(d - 1, -1, -1):
                        memo[x_fen[i].n] = True

                    for i in range(n):
                        if memo[i]:
                            leng += fen[i].z
                            key += 1

                    for i in range(n):
                        if ((y_fen[r].y - y_fen[l].y) + (x_fen[u].x - x_fen[d].x)) * 2 <= leng:
                            break
                        if memo[i]:
                            continue
                        leng += fen[i].z
                        key += 1

                    if ((y_fen[r].y - y_fen[l].y) + (x_fen[u].x - x_fen[d].x)) * 2 <= leng:
                        ans = min(ans, key)
    print(ans)

if __name__ == '__main__':
    main()