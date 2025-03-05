#1013
import re
from sys import stdin
input = stdin.readline

n = int(input())
res = []

for _ in range(n):
    tmp = input().replace('\n', '')
    a = re.compile('(100+1+|01)+')
    b = a.fullmatch(tmp)
    if b: res.append("YES")
    else: res.append("NO")

for ans in res:
    print(str(ans))


