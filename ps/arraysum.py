#2143
import bisect
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    a = int(input())
    alist = list(map(int, input().split()))
    b = int(input())
    blist = list(map(int, input().split()))

    list1, list2 = [], []
    for i in range(a):
        for j in range(i + 1, a + 1):
            list1.append(sum(alist[i : j]))
    for i in range(b):
        for j in range(i + 1, b + 1):
            list2.append(sum(blist[i : j]))

    list1.sort()
    list2.sort()

    ans = 0
    for i in range(len(list1)):
        tmp = n - list1[i]
        left = bisect.bisect_left(list2, tmp)
        right = bisect.bisect_right(list2, tmp)
        ans += (right - left)
    print(ans)

if __name__ == '__main__':
    main()