from itertools import combinations
from sys import stdin
input = stdin.readline

n = int(input())
ans = []

def main():
    for i in range(1, 11):
        for j in combinations(range(10), i):
            num = ''.join(list(map(str, reversed(list(j)))))
            ans.append(int(num))

    ans.sort()
    print(-1 if n >= len(ans) else ans[n])

if __name__ == '__main__':
    main()
