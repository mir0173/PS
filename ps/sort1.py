#1083
from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    if m == 0:
        print(*arr)
        return
    for i in range(n - 1):
        key, index = arr[i], i
        for j in range(i + 1, min(n, i + 1 + m)):
            if key < arr[j]:
                key, index = arr[j], j
        m -= index - i
        for j in range(index, i, -1): arr[j] = arr[j - 1]
        arr[i] = key
        
    print(*arr)

if __name__ == '__main__':
    main()