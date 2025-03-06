#1060
from sys import stdin
input = stdin.readline

def main():
    l = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    n = int(input())
    tmp_arr, ans, q = [], [], 0

    if arr[0] == 2: ans.append([0, 1])
    elif arr[0] > 2: tmp_arr.append([arr[0] - 1, 1]); q += 1

    for i in range(l-1):
        if arr[i + 1] - arr[i] - 1 == 1: ans.append([0, arr[i] + 1])
        else: tmp_arr.append([arr[i + 1] - arr[i] - 1, arr[i] + 1]); q += 1
    tmp_arr.sort()
    for i in arr: ans.append([0,i])

    for a, b in tmp_arr:
        p, q, r = 0, a//2, 0
        while p < q and r < n:
            m = 0
            if p > 1: m = sum(range(p))
            ans.extend([[sum(range(a - 1, a - p - 2, -1)) - m, b + p], [sum(range(a - 1, a - p - 2, -1)) - m, b + a - 1 - p]])
            p += 1
            r += 2
        if a % 2:
            m = 0
            if p > 1: m = sum(range(p))
            ans.append([sum(range(a - 1,a - p - 2, -1)) - m,b + p])
    ans.sort()
    p, r = len(ans), 1
    while p < n: ans.append([0, arr[l - 1] + r]); p += 1; r += 1

    print(*[ans[i][1] for i in range(n)])

if __name__ == '__main__':
    main()