# 1036
from sys import stdin
input = stdin.readline
from collections import deque
string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
ans = 0
List = [0] * 36

def dif(num):
    length = len(num)
    for i in range(length):
        n = int(num[length - i - 1], 36)
        List[n] += (35 - n) * (36 ** i)

def three_six(x):
    if x == 0:
        return 0
    d = deque()
    while x:
        d.extendleft(string[x % 36])
        x //= 36
    return "".join(d)

def main():
    global ans
    for i in range(n):
      num = input().strip()
      ans += int(num, 36)
      dif(num)
    List.sort(reverse = True)

    k = int(input())
    for i in range(k):
      ans += List[i]

    print(three_six(ans))

if __name__ == '__main__':
    main()