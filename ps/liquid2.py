#2470
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    liq = sorted(list(map(int, input().split())))
    start, end = 0, n - 1
    answer = [liq[start], liq[end]]
    ans = abs(liq[start] + liq[end])

    while start < end:
        l, r = liq[start], liq[end]
        sum = l + r
        if abs(sum) < ans:
            ans = abs(sum)
            answer = [l, r]
            if ans == 0: break

        if sum < 0:
            start += 1
        else:
            end -= 1
    print(*answer)

if __name__ == '__main__':
    main()