#3806
from sys import stdin
input = stdin.readline
ans_list = []

def main():
    t = int(input())
    for k in range(1, t + 1):
        s = list(input().rstrip())
        t = list(input().rstrip())
        sLen = len(s)
        case1, case2, case3, case4 = 0, 0, 0, 0

        for i in range(sLen):
            a, b = s[i], t[i]
            if a == '0' and b == '1': case1 += 1
            elif a == '1' and b == '0': case2 += 1
            elif a == '?' and b == '0': case3 += 1
            elif a == '?' and b == '1': case4 += 1

        ans = 0
        tmp1 = min(case1, case2)
        case1, case2, ans = case1 - tmp1, case2 - tmp1, ans + tmp1
        tmp1 = min(case4, case2)
        case2, case3, case4, ans = case2 - tmp1, case3 + tmp1, case4 - tmp1, ans + tmp1
        ans = case1 + case3 + case4 + ans

        if case2 > 0: ans = -1
        ans_list.append("Case %d: %d" % (k, ans))
    print(*ans_list, sep='\n')

if __name__ == '__main__':
    main()