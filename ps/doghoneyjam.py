#7726
from sys import stdin
input = stdin.readline

def cal_sum(arr, n, m):
    sum_arr = [[0] * (m + 1) for _ in range(n + 1)]
    dp = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sum_arr[i][j] = arr[i - 1][j - 1] + sum_arr[i - 1][j] + sum_arr[i][j - 1] - sum_arr[i - 1][j - 1]

    for a in range(1, n):  
        for b in range(1, m): 
            for c in range(a, n + 1):  
                for d in range(b , m + 1):  
                    sub_sum = sum_arr[c][d] - sum_arr[a - 1][d] - sum_arr[c][b - 1] + sum_arr[a - 1][b - 1]
                    dp.append([sub_sum, a - 1, b - 1, c - 1, d - 1])
    return dp

def max_sum(matrix, k):
    matrix.sort(reverse = True,key=lambda x: x[0])
    sum = matrix[0][0]
    new_matrix = [matrix[0]]
    for i in range(1, len(matrix)):
        for j in range(len(new_matrix)):
            if matrix[i][3] < new_matrix[j][1] or matrix[i][1] > new_matrix[j][3] or matrix[i][2] > new_matrix[j][4] or matrix[i][4] < new_matrix[j][2]:
                sum += matrix[i][0]
                new_matrix.append(matrix[i])
        if len(new_matrix) == k:
            return sum

def main():
    n, m, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    dp = cal_sum(matrix, n, m)
    print(max_sum(dp, k))

if __name__ == '__main__':
    main()
    
# 썅 메모리 ㅈㄴ쓰네 으아아아아아ㅏㅇ아ㅏ각