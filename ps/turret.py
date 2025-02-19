from sys import stdin
input = stdin.readline
import math
ans = []

def main():
    n = int(input())
    for _ in range(n):
        a1, b1, c1, a2, b2, c2 = map(int, input().split())
        d = math.sqrt(math.pow(a2 - a1, 2) + math.pow(b2 - b1, 2))
        if a1 == a2 and b1 == b2 and c1 == c2:
            ans.append(-1)
        elif c1 + c2 > d > abs(c1 - c2):
            ans.append(2)
        elif c1 + c2 == d or abs(c1 - c2) == d:
            ans.append(1)
        else:
            ans.append(0)

    for i in ans:
        print(i)

if __name__ == '__main__':
    main()