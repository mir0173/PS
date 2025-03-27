#15311
from sys import stdin
input = stdin.readline
N = int(input())
result = []
for i in range(1000): result.append(1)
for j in range(1000): result.append(1000)
print(len(result))
print(*result)