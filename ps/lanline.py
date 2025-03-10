#1654
from sys import stdin
input = stdin.readline

need, n = map(int, input().split())
lan = [int(input()) for _ in range(need)]
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in lan:
        lines += i // mid

    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)