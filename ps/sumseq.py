from sys import stdin
input = stdin.readline

def main():
    n, l = map(int, input().split())
    for i in range(l, 101):
        x = n / i - (i + 1)/2
        if x.is_integer():
            if x + 1 >= 0:
                for j in range(int(x) + 1, int(x) + i + 1):
                    print(j, end=" ")
                break
    else:
        print(-1)

if __name__ == '__main__':
    main()