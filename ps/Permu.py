#1115
from sys import stdin
input = stdin.readline
n = int(input())
a = list(map(int, input().split()))
arr = [False] * n
cnt = 0

for i in range(n):
    if not arr[i]:
        cnt += 1
        arr[i] = True
        j = a[i]
        while j != i:
            arr[j] = True
            j = a[j]

print(0 if cnt == 1 else cnt)