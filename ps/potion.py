from sys import stdin
input = stdin.readline
from collections import defaultdict
N, M = map(int, input().split())
dic = defaultdict(lambda: -1)
mat = [[] for _ in range(51)]

def main():
    for _ in range(N):
        val, a = input().split()
        dic[val] = int(a)

    for i in range(M):
        val = input().strip()
        num = 0
        s = ""

        while val[num] != '=':
            s += val[num]
            num += 1
        mat[i].append((0, s))

        if s not in dic:
            dic[s] = -1

        while num < len(val):
            tmp = ""
            num += 1
            if num >= len(val):
                break
            comat = int(val[num])
            num += 1
            while num < len(val) and val[num] != '+':
                tmp += val[num]
                num += 1
            mat[i].append((comat, tmp))
            if tmp not in dic:
                dic[tmp] = -1

    for i in range(M):
        for j in range(M):
            cost = 0
            make = mat[j][0][1]
            key = True
            for k in range(1, len(mat[j])):
                if dic[mat[j][k][1]] == -1:
                    key = False
                    break
                cost += dic[mat[j][k][1]] * mat[j][k][0]
                if cost > 1000000000:
                    cost = 1000000001
            if key:
                if dic[make] == -1:
                    dic[make] = cost
                else:
                    dic[make] = min(dic[make], cost)
    print("-1" if "LOVE" not in dic or dic["LOVE"] == -1 else dic["LOVE"])

if __name__ == "__main__":
    main()
