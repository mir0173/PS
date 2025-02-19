from sys import stdin
input = stdin.readline
n = int(input())
answer = []

def main():
    for _ in range(n):
        x, y = map(int, input().split())
        d = y - x
        now = 0
        ans = 0
        try_num = 0

        while now < d:
            ans += 1
            try_num += 1 if ans % 2 else 0
            now += try_num
        answer.append(ans)

    for i in range(n):
        print(answer[i])

if __name__ == '__main__':
    main()