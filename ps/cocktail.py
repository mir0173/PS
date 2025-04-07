#1033
from sys import stdin
input = stdin.readline

def gcd(a, b):
    if a%b == 0: return b
    return gcd(b, a%b)

def dfs(r):
    v[r] = True
    for i in adj[r]:
        if not v[i[0]]:
            mass[i[0]] = i[2] * mass[r] // i[1]
            dfs(i[0])

def main():
    global adj, v, mass
    n = int(input())
    adj = [[] for _ in range(n)]
    mass = [0] * n
    v = [False] * n
    tmp = 1
    
    for _ in range(n - 1):
        a, b, p, q = map(int,input().split())
        adj[a].append((b, p, q))
        adj[b].append((a, q, p))
        tmp *= ((p * q) // gcd(p, q))
        
    mass[0] = tmp
    dfs(0)
    gcd_ans = mass[0]
    for i in range(n): gcd_ans = gcd(gcd_ans, mass[i])
    for i in range(len(mass)): mass[i] //= gcd_ans
    print(*mass)

if __name__ == '__main__':
    main()