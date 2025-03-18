#15961
from sys import stdin
input = stdin.readline

def main():
    n, m, l, k = map(int,input().split())
    key = 1
    data = [int(input()) for _ in range(n)]
    arr = [0] * (m + 1)
    arr[k] = 1

    for i in range(l):
        arr[data[i]] += 1
        if arr[data[i]] == 1: key += 1

    ans = key
    for i in range(n - 1):
        arr[data[i]] -= 1
        if arr[data[i]] == 0: key -= 1
        arr[data[(i + l) % n]] += 1
        if arr[data[(i + l) % n]] == 1: key += 1
        ans = max(ans, key)

    print(ans)

if __name__ == '__main__':
    main()