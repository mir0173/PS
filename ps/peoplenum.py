#1206
from sys import stdin
input = stdin.readline
import math

def check(key, float_list):
    for float_num in float_list:
        l, r = 0, key * 10
        while l < r:
            mid = (l + r) // 2
            if (mid / key) < float_num: l = mid + 1
            else: r = mid
        if math.floor((l / key * 1000)) / 1000 != float_num: return False
    return True

def main():
    n = int(input())
    float_list = [float(input()) for _ in range(n)]
    key = 0
    while key < 1000:
        key += 1
        if check(key, float_list): break
    print(key)

if __name__ == '__main__':
    main()