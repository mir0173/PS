#1917
from sys import stdin
input = stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dk = [1, 0, 3, 2]

def move(k) :
  if k == 0: visit[0][1], visit[1][1], visit[2][1], visit[3][1] = visit[3][1], visit[0][1], visit[1][1], visit[2][1]
  elif k == 1: visit[0][1], visit[1][1], visit[2][1], visit[3][1] = visit[1][1], visit[2][1], visit[3][1], visit[0][1]
  elif k == 2: visit[1][0], visit[1][1], visit[1][2], visit[3][1] = visit[3][1], visit[1][0], visit[1][1], visit[1][2]
  else: visit[1][0], visit[1][1], visit[1][2], visit[3][1] = visit[1][1], visit[1][2], visit[3][1], visit[1][0]

def dfs(x, y) :
    ans = 1
    for k in range(4) :
        ax, ay = x + dx[k], y + dy[k]
        if -1 < ax < 6 and -1 < ay < 6 and adj[ay][ax] == 1 :
            move(k)
            if not visit[1][1] :
                visit[1][1] = True
                ans += dfs(ax, ay)
            move(dk[k])
    return ans

def main():
    global ans, visit, adj
    for _ in range(3) :
        adj = [list(map(int, input().split())) for _ in range(6)]
        visit = [[False] * 3 for _ in range(4)]
        tmp = False
        for i in range(6) :
            for j in range(6) :
                if adj[i][j] == 1 :
                    visit[1][1] = True
                    ans = dfs(j, i)
                    tmp = True
                    break
            if tmp :
                break
        print('yes' if ans == 6 else 'no')

if __name__ == '__main__':
    main()