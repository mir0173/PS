#1027
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    List = list(map(int, input().split()))
    ans = 0
    for i, y1 in enumerate(List):
        x1 = i + 1
        isRight, right = None, 0
        for j in range(i + 1, n + 1):
            if j == n: break
            x2, y2 = j + 1, List[j]
            if isRight is None or isRight < (y2 - y1) / (x2 - x1):
                isRight = (y2 - y1) / (x2 - x1)
                right += 1

        isLeft, left = None, 0
        for k in range(i - 1, -1, -1):
            if k == -1: break
            x2, y2 = k + 1, List[k]
            if isLeft is None or isLeft > (y2 - y1) / (x2 - x1):
                isLeft = (y2 - y1) / (x2 - x1)
                left += 1

        if (left + right) > ans: ans = left + right

    print(ans)

if __name__ == '__main__':
    main()