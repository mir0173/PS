#2473
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    List = list(map(int, input().split()))
    List.sort()
    Min = 3e9
    for i in range(n - 2):
        start, end = i + 1, n - 1
        while start < end:
            tmp = List[i] + List[start] + List[end]
            if abs(tmp) < Min:
                Min = abs(tmp)
                ans = [List[i], List[start], List[end]]
            if tmp < 0:
                start += 1
            elif tmp > 0:
                end -= 1
            else:
                break
    print(*ans)

if __name__ == '__main__':
    main()