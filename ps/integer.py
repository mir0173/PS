#1040
from sys import stdin
input = stdin.readline
from itertools import combinations, combinations_with_replacement

def integer(n, k):
    if len(set(n)) == k: return n

    for i in range(1, len(n) + 1):
        result = []
        u = n[:-i]
        use = set(u)
        nuse = set(map(str, range(10))) - use
        key = k - len(use)
        if 0 <= key <= i:
            for comb1 in combinations(nuse, key):
                comb1 = set(comb1)
                for comb2 in combinations_with_replacement(use | comb1, i - key):
                    wuse = [*comb2, *comb1]
                    for j in range(int(n[-i]) + 1, 10):
                        j = str(j)
                        if j in wuse:
                            wuse.remove(j)
                            result.append(u + j + "".join(sorted(wuse)))

            if result: return min(result)

    return "1" + "0" * (max(len(n) + 1, k) - k + 1) + "".join(map(str, range(2, k)))

def main():
    n, k = input().split()
    k = int(k)
    ans = integer(n, k)
    print(ans)

if __name__ == "__main__":
    main()