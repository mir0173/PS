#2305
from sys import stdin
input = stdin.readline

n = int(input())
k = int(input())
arr = []
bool_list = [False] * (n + 1)
adj = [[[[-1] * 2 for _ in range(5)] for _ in range(5)] for _ in range(n + 1)]

def dp(idx, pp, p, key):
    if idx == n - 1: return 1
    if adj[idx][pp][p][key] != -1: return adj[idx][pp][p][key]
    adj[idx][pp][p][key] = 0
    if not key: adj[idx][pp][p][key] += dp(idx + 1, p, 3, 1 - key)
    if p != 2: adj[idx][pp][p][key] += dp(idx + 1, p, 0, key)
    if p != 0 and pp != 2:
        if arr[idx] - 1 >= 1 and not bool_list[arr[idx] - 1]: adj[idx][pp][p][key] += dp(idx + 1, p, 1, key)
    if arr[idx] + 1 <= n and not bool_list[arr[idx] + 1]: adj[idx][pp][p][key] += dp(idx + 1, p, 2, key)
    return adj[idx][pp][p][key]

def main():
    for i in range(1, n + 1):
        if i == k:
            bool_list[i] = True
            continue
        arr.append(i)
    print(dp(0, -1, -1, 0))

if __name__ == "__main__":
    main()