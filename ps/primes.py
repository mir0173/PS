from sys import stdin
input = stdin.readline

def dfs(x, visit, Y, primes, mat):
    if visit[Y.index(x)]: return False
    visit[Y.index(x)] = True
    for y in Y:
        if x + y in primes:
            if y not in mat or dfs(mat[y], visit, Y, primes, mat):
                mat[y] = x
                return True
    return False

def main():
    N = int(input())
    X = list(map(int, input().split()))
    primes = []
    ans = []
    
    for i in range(2, 2000):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    
    for i in X:
        mat = {}
        if i == X[0]:
            continue
        if X[0] + i in primes:
            if N == 2:
                ans.append(i)
                break
            Y = [x for x in X]
            del Y[0]
            del Y[Y.index(i)]
            mat = {}
            for y in Y:
                visit = [False for _ in range(len(Y))]
                dfs(y, visit, Y, primes, mat)
        if N != 2 and len(mat) == N - 2:
            ans.append(i)

    print(-1) if not ans else print(*sorted(ans))

if __name__ == '__main__':
    main()