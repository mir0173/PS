#20040
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
list1 = [i for i in range(n)]
list2 = [0 for _ in range(n)]
list3 = [0 for _ in range(m)]

def union(x1, x2):
    y1, y2 = find(x1), find(x2)

    if list2[y1] > list2[y2]:
        list1[y2] = y1
    elif list2[y1] < list2[y2]:
        list1[y1] = y2
    else:
        list1[y2] = y1
        list2[y1] += 1

def find(x):
    if x == list1[x]:
        return x
    list1[x] = find(list1[x])
    return list1[x]

def main():
    ans = 0
    for i in range(m):
        a, b = map(int, input().split())
        if find(a) == find(b):
            ans = i + 1
            break
        union(a, b)
    print(ans)

if __name__ == '__main__':
    main()
