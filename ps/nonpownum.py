from sys import stdin
input = stdin.readline
import math

def non_pow(a, b):
    List = [True for _ in range(b - a + 1)]

    for i in range(2, int(math.sqrt(b)) + 1):
        n = i * i
        start = max(n, (a + n - 1) // n * n)
        for j in range(start, b + 1, n):
            List[j - a] = False

    print(sum(List))

def main():
    a, b = map(int, input().split())
    non_pow(a, b)

if __name__ == '__main__':
    main()