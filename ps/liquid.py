#2467
from sys import stdin
input = stdin.readline

def main():
    min = 2e9
    N = int(input())
    x, y = 0, 0
    l = 0
    r = N - 1
    liq = list(map(int, input().split()))

    while l < r:
        val = liq[l] + liq[r]

        if abs(val) <= min:
            x = liq[l]
            y = liq[r]
            min = abs(val)

        if val <= 0:
            l += 1
        else:
            r -= 1

    print(x, y)

if __name__ == '__main__':
    main()