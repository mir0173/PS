#27172
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    List = list(map(int, input().split()))
    Set = set(List)
    m = max(List)
    ans = [0 for _ in range(m + 1)]

    for i in List:
        if i == m: continue
        for j in range(2 * i, m + 1, i):
            if j in Set:
                ans[i] += 1
                ans[j] -= 1
    for i in List:
        print(ans[i], end = ' ')

if __name__ == '__main__':
    main()