#1041
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    a, b, c, d, e, f = map(int, input().split())
    one = min(a, b, c, d, e, f)
    two = min(a + b, a + c, a + d, a + e, f + b, f + c, f + d, f + e, b + c, b + d, c + e, d + e)
    three = min(a + b + c, a + b + d, a + c + e, a + d + e, f + b + c, f + b + d, f + c + e, f + d + e)
    if n == 1:
        print(sum( sorted([a, b, c, d, e, f])[:-1]))
    else:
        print(((n - 2) ** 2 * 5 + 4 * (n - 2)) * one + (8 * (n - 2) + 4) * two + 4 * three)

if __name__ == '__main__':
    main()

