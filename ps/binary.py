#2201
from sys import stdin
input = stdin.readline
n = int(input())
max = 86
dp, sum = [[0, 0] for _ in range(max + 1)], [0] * (max + 1)
dp[1][1] = sum[1] = 1

def main():
    global n
    for i in range(2, max + 1):
        dp[i][0] , dp[i][1] = dp[i - 1][0] + dp[i - 1][1], dp[i - 1][0]
        sum[i] = dp[i][0] + dp[i][1] + sum[i - 1]
    
    if n == 1:
        print(1)
    else:
        print(1, end="")
        for i in range(2, max + 1):
            if n <= sum[i]:
                tmp = i
                break

        n -= sum[tmp - 1] + 1
        tmp -= 1
        while tmp > 0:
            if n > sum[tmp - 1]:
                print(1, end="")
                n -= sum[tmp - 1] + 1
            else:
                print(0, end="")
            tmp -= 1

if __name__ == '__main__':
    main()