#1058
def main():
    n = int(input())
    fri = [list(input()) for _ in range(n)]
    con = [[0] * n for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if fri[i][j] == "Y" or (fri[i][k] == "Y" and fri[k][j] == "Y"):
                    con[i][j] = 1

    ans = 0
    for r in con:
        ans = max(ans, sum(r))
    print(ans)

if __name__ == '__main__':
    main()