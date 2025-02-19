from itertools import combinations
from sys import stdin
input = stdin.readline

def f(x, n): return (x * x + 1) % n

def gcd(a, b):
    while b: 
        a, b = b, a % b
    return a

def fast_pow(a, b, m):
    val = 1
    while b:
        if b % 2: val = val * a % m
        a = a * a % m
        b //= 2
    return val

def prime(n, a):
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    x = fast_pow(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(r - 1):
        x = fast_pow(x, 2, n)
        if x == n - 1:
            return True
    return False

def isprime(n):
    if n <= 79:
        return n in {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79}
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if not prime(n, a): 
            return False
    return True

def pol(n, m):
    if isprime(n): 
        return n
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]:
        if n % p == 0: 
            return p
    l, d = m, 1
    while d == 1:
        m = f(m, n)
        l = f(f(l, n), n)
        d = gcd(abs(m - l), n)
    return pol(n, m + 1) if d == n else pol(d, m + 1)

def main():
    num = int(input())
    number, ans = num, []
    while num != 1:
        k = pol(num, 2)
        ans.append(k)
        num //= k
    ans, sum = set(ans), number
    for i in range(1, len(ans) + 1):
        for j in combinations(ans, i):
            k = 1
            for p in j: k *= p
            sum += (number // k) * (-1 if i % 2 else 1)
    print(sum if number > 1 else 1)

if __name__ == '__main__':
    main()