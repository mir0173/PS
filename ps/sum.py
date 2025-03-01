#1081
from sys import stdin
input = stdin.readline

def digit_sum(n):
    if n <= 0:
        return 0
    num, sum, key = [0] * 10, 0, 1

    while n > 0:
        x = n // (key * 10)
        y = n % (key * 10)
        for i in range(10):
            num[i] += x * key
        for i in range(1, y // key + 1):
            num[i] += key
        num[(y // key + 1) % 10] += y % key
        n -= 9 * key
        key *= 10

    for i in range(1, 10):
        sum += i * num[i]
    return sum

def main():
    a, b = map(int, input().split())
    print(digit_sum(b) - digit_sum(a - 1))

if __name__ == '__main__':
    main()