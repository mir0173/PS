#16724
from sys import stdin
input = stdin.readline

n, m = map(int,input().split())
Map = list(list(map(str, input())) for _ in range(n))
adj = [[-1 for _ in range(m)] for _ in range(n)]
dir = ['L','R','U','D']
dx = [0,0,-1,1]
dy = [-1,1,0,0]
ans = 0

def move(x, y, index):
    global ans
    if adj[x][y] != -1:
        if adj[x][y] == index:
            ans += 1
        return

    adj[x][y] = index
    i = dir.index(Map[x][y])
    move(x + dx[i], y + dy[i], index)

def main():
    index = 0
    for i in range(n):
        for j in range(m):
            move(i, j, index)
            index += 1
    print(ans)

if __name__ == '__main__':
    main()