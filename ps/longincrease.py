#14003 12015
import bisect
from sys import stdin
input = stdin.readline

n = int(input())
List = list(map(int, input().split()))
dp = [-1e10]
ans = []
answer = []

for i in range(n):
    if dp[-1] < List[i]:
        dp.append(List[i])
        ans.append((len(dp) - 1, List[i]))
    else:
        pos = bisect.bisect_left(dp, List[i])
        dp[pos] = List[i]
        ans.append((pos, List[i]))
tmp = len(dp) - 1
print(tmp)

for i in range(len(ans)-1, -1, -1):
    if ans[i][0] == tmp:
        answer.append(ans[i][1])
        tmp -= 1

print(*answer[::-1])