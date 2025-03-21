#1003
from sys import stdin
input = stdin.readline
def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        a, b = 1, 0
        for i in range(m): a, b = b, a + b
        print(a,b)

if __name__ == '__main__':
    main()
