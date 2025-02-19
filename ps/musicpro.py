from sys import stdin
input = stdin.readline

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    ans = []

    for _ in range(m):
        arr = list(map(int, input().split()))
        for i in range(1, arr[0]):
            adj[arr[i]].append(arr[i + 1])
            deg[arr[i + 1]] += 1

    queue = []
    for i in range(1, n + 1):
        if deg[i] == 0:
            queue.append(i)

    while queue:
        p = queue.pop(0)
        ans.append(p)
        for i in adj[p]:
            deg[i] -= 1

            if deg[i] == 0:
                queue.append(i)

    if len(ans) == n:
        print(*ans, sep = "\n")
    else:
        print(0)

if __name__ == '__main__':
    main()