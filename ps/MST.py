from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
List = list(range(n + 1))

def find(x):
    if List[x] != x:
        List[x] = find(List[x])
    return List[x]

def none_cycle(x, y):
    x_index = find(x)
    y_index = find(y)
    if x_index != y_index:
        List[y_index] = x_index

def main():
    edge = []
    ans = 0

    for i in range(1, m + 1):
        a, b, c = map(int, input().split())
        edge.append((c, a, b))
    edge.sort()

    for c, a, b in edge:
        if find(a) != find(b):
            none_cycle(a, b)
            ans += c

    print(ans)

if __name__ == '__main__':
    main()