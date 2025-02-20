#1647
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
edges = []
List = list(range(n + 1))

def find(n):
    if List[n] != n:                  
        List[n] = find(List[n])     
    return List[n]                   

def union(a, b):
    a = find(a)        
    b = find(b)         
    if a < b:           
        List[b] = a   
    else:              
        List[a] = b   

def main():
    for _ in range(m):
        a, b, key = map(int, input().split())
        edges.append((a, b, key))
    edges.sort(key = lambda x: x[2])
    
    answer = 0
    minus = 0
    for c, d, key2 in edges:
        if find(c) != find(d):
            union(c, d)
            answer += key2
            minus = key2
    print(answer - minus)

if __name__ == '__main__':
    main()