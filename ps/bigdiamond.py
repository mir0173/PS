from sys import stdin
input = stdin.readline

def diamond(n, m, arr):
    left_down = [[0] * (m + 2) for _ in range(n + 2)]
    right_down = [[0] * (m + 2) for _ in range(n + 2)]
    left_up = [[0] * (m + 2) for _ in range(n + 2)]
    right_up = [[0] * (m + 2) for _ in range(n + 2)]

    for i in range(n, 0, -1):
        for j in range(1, m + 1):
            if arr[i - 1][j - 1] == 1:
                left_down[i][j] = left_down[i + 1][j - 1] + 1 if i + 1 <= n and j - 1 >= 1 else 1
                right_down[i][j] = right_down[i + 1][j + 1] + 1 if i + 1 <= n and j + 1 <= m else 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i - 1][j - 1] == 1:
                left_up[i][j] = left_up[i - 1][j - 1] + 1 if i - 1 >= 1 and j - 1 >= 1 else 1
                right_up[i][j] = right_up[i - 1][j + 1] + 1 if i - 1 >= 1 and j + 1 <= m else 1

    ans = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, min(left_down[i][j], right_down[i][j]) + 1):
                if i + 2 * (k - 1) - 1 < n and \
                        left_up[i + 2 * (k - 1)][j] >= k and \
                        right_up[i + 2 * (k - 1)][j] >= k:
                    ans = max(ans, k)

            for k in range(1, min(right_up[i][j], right_down[i][j]) + 1):
                if j + 2 * (k - 1) - 1 < m and \
                        left_up[i][j + 2 * (k - 1)] >= k and \
                        left_down[i][j + 2 * (k - 1)] >= k:
                    ans = max(ans, k)

    return ans

def main():
    n, m = map(int, input().split())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    print(diamond(n, m, arr))

if __name__ == "__main__":
    main()
