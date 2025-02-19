#10942
import sys
input = sys.stdin.readline

n = int(input())
List = list(map(int, input().split()))
dp = [[0]*n for i in range(n)]

for i in range(n):
    dp[i][i] = 1
    
for i in range(n - 1):
    dp[i][i+1] = 1 if List[i]==List[i+1] else 0
    
for i in range(n - 2):
    for j in range(n - 2 - i):
        k = j + 2 + i
        if List[j] == List[k] and dp[j+1][k-1] == 1:
            dp[j][k] = 1

def main():
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        print(dp[a-1][b-1])

if __name__ == '__main__':
    main()