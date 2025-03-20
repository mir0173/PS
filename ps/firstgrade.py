#5557
from sys import stdin
input = stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

def main():
    dp = [0] * 21
    dp[n_list[0]] = 1

    for num in n_list[1:-1]:
        tmp = [0] * 21
        for total in range(21):
            if dp[total]:
                if total + num <= 20:
                    tmp[total + num] += dp[total]
                if total - num >= 0:
                    tmp[total - num] += dp[total]
        dp = tmp

    print(dp[n_list[-1]])

if __name__ == '__main__':
    main()