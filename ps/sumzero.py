#7453
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ablist, cdlist = [], []
    for i in range(n):
        for j in range(n):
            ablist.append(arr[i][0] + arr[j][1])
            cdlist.append(arr[i][2] + arr[j][3])

    ablist.sort()
    cdlist.sort()

    i, j = 0, len(cdlist) - 1  
    ans = 0
    while i < len(ablist) and j >= 0:
        if ablist[i] + cdlist[j] == 0:  
            x, y = i + 1, j - 1
            while x < len(ablist) and ablist[i] == ablist[x]:
                x += 1
            while y >= 0 and cdlist[j] == cdlist[y]:
                y -= 1
            ans += (x - i) * (j - y)
            i, j = x, y

        elif ablist[i] + cdlist[j] < 0:
            i += 1
        else:
            j -= 1

    print(ans)
    
if __name__ == '__main__':
    main()
