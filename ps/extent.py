from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    x = []
    y = []
    ans = 0
    for i in range(n):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)

    for i in range(n - 1):
        ans += x[i] * y[i + 1] - x[i + 1] * y[i]
    ans += x[n - 1] * y[0] - x[0] * y[n - 1]
    ans = abs(ans) / 2
    print(round(ans, 1))

if __name__ == '__main__':
    main()

