#1112
from sys import stdin
input = stdin.readline

def main():
    a, b = map(int, input().split())
    n = 0
    ans = []
    tmp = 0

    if a < 0 < b:
        a *= -1
        tmp = 1

    while a:
        x, y = divmod(a, b)
        if y < 0:
            y -= b
            x += 1
        ans.append(y)
        a = x

    if not ans:
        ans.append(0)
    ans.reverse()

    if tmp:
        ans[0] *= -1
    print(''.join(map(str, ans)))

if __name__ == '__main__':
    main()