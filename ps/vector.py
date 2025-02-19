import math
n = int(input())

def choose(points, a):
    plist = list(points)
    n = len(plist)
    result = []

    def recus(start, List):
        if len(List) == a:
            result.append(tuple(List))
            return

        for i in range(start, n):
            recus(i + 1, List + [plist[i]])

    recus(0, [])
    return result

def main():
    for _ in range(n):
        m = int(input())
        point = []
        xall, yall = 0, 0

        for _ in range(m):
            x, y = map(int, input().split())
            xall += x
            yall += y
            point.append((x, y))

        List = list(choose(point, m // 2))
        ans = math.inf

        for i in List[:len(List) // 2]:
            x1, y1 = 0, 0
            for x, y in i:
                x1 += x
                y1 += y
            x2, y2 = xall - x1, yall - y1

            vec = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
            ans = vec if vec < ans else ans
        print(ans)

if __name__ == '__main__':
    main()