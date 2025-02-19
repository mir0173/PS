import math
from sys import stdin
input = stdin.readline
ans = []

def range2(start, end, inc):
    x = []
    while True:
        x.append(start)
        start += inc
        if start >= end:
            break
    return x

def simulate_case(m, b, d, t):
    for i in range2(t + 5 / m, t + 6 / m, 1e-5):
        for j in range(1, 11):
            if -d + i * b - 4 * (j - 1) - 2 < math.sqrt(0.25 - math.pow(0.5 - m * (i - (t + 5 / m)), 2))< -d + i * b - 4 * (j - 1) or -d + i * b - 4 * (j - 1) - 2 < -math.sqrt(0.25 - math.pow(0.5 - m * (i - (t + 5 / m)), 2)) < -d + i * b - 4 * (j - 1):
                return f"Collision with bicycle {j}"
    if -d + (t + 6 / m) * b <= 0:
        return "Max beats the first bicycle"
    for k in range(1, 10):
        if -d + (t + 6 / m) * b - 4 * (k - 1) - 4 <= 0 <= -d + (t + 6 / m) * b - 4 * (k - 1) - 2:
            return f"Max crosses safely after bicycle {k}"
    return f"Max crosses safely after bicycle 10"

def main():
    N = int(input())

    for _ in range(N):
        M = float(input())
        B = float(input())
        D = float(input())
        T = float(input())

        ans.append(simulate_case(M, B, D, T))

    for l in range(N):
        print(ans[l])

if __name__ == '__main__':
    main()
