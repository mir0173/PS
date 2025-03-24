from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    r, g, b = [], [], []
    for i in range(n):
        line = input().strip()
        for j, c in enumerate(line):
            if c == 'R': r.append((i, j))
            elif c == 'G': g.append((i, j))
            elif c == 'B': b.append((i, j))
    
    print(get(r, g, b))

def ccw(a, b, c): return a[0] * b[1] - a[1] * b[0] + b[0] * c[1] - b[1] * c[0] + c[0] * a[1] - c[1] * a[0]

def conv(points):
    h1, h2 = [], []
    if len(points) <= 1: return points
    points.sort()
    for p in points:
        while len(h1) >= 2 and ccw(h1[-2], h1[-1], p) < 0: h1.pop()
        h1.append(p)
    points.reverse()
    for p in points:
        while len(h2) >= 2 and ccw(h2[-2], h2[-1], p) < 0: h2.pop()
        h2.append(p)
    return list(dict.fromkeys(h1 + h2))

def most(a, b, points):
    limit = -1
    res = []
    for p in points:
        area = abs(ccw(a, b, p))
        if area > limit: limit = area; res = [p]
        elif area == limit: res.append(p)
    return res

def get(r, g, b):
    if not r or not g or not b: return 0
    R, G, B = map(conv, [r, g, b])
    key = len(r) * len(g) * len(b)
    for r1 in R:
        for g1 in G:
            for b1 in most(r1, g1, B):
                fr = most(g1, b1, R)[0]
                area = abs(ccw(b1, r1, g1))
                if abs(ccw(fr, g1, b1)) != area: continue
                fg = most(b1, r1, G)[0]
                if abs(ccw(fg, b1, r1)) != area: continue
                key -= 1
    return key

if __name__ == '__main__':
    main()