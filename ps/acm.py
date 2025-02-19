from collections import deque
from sys import stdin
input = stdin.readline
task = int(input())
ans= []

def main():
    for _ in range(task):
        n, m = map(int, input().split()) 
        val = [0] + list(map(int, input().split())) 
        adj = [[] for _ in range(n + 1)]
        archi = [0] * (n + 1)
        
        for _ in range(m): 
            a, b = map(int ,input().split())
            adj[a].append(b)
            archi[b] += 1
    
        Queue = deque()
        dp = [0] * (n + 1)
        end = int(input())
        
        for i in range(1, n + 1): 
            if archi[i] == 0:
                Queue.append(i)
                dp[i] = val[i]
    
        while Queue:
            tmp = Queue.popleft()
            for j in adj[tmp]:
                archi[j] -= 1
                dp[j] = max(dp[tmp] + val[j], dp[j])
                if archi[j] == 0:
                    Queue.append(j)
                    
        ans.append(dp[end])
    
    for answer in ans:
        print(answer)

if __name__ == '__main__':
    main()