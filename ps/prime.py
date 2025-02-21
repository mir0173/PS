#1644
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    a = [False, False] + [True] * (n - 1)
    prime = []

    for i in range(2, n + 1):
        if a[i]:
            prime.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False

    ans, start, end = 0, 0, 0
    while end <= len(prime):
        if sum(prime[start:end]) == n:
            ans += 1
            end += 1
        elif sum(prime[start:end]) < n:
            end += 1
        else:
            start += 1

    print(ans)

if __name__ == '__main__':
    main()