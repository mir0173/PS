import math
a, b = map(int, input().split())
isprime = [False] * (b + 1)
task = [0] * (b + 1)

def main():
    isprime = [False] * (b + 1)
    task = [0] * (b + 1)

    for i in range(2, b + 1):
        isprime[i] = True
        if i > 3:
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    task[i] = task[i // j] + 1
                    isprime[i] = False
                    break
        if isprime[i]:
            task[i] = 1

    ans = 0
    for i in range(a, b + 1):
        ans += isprime[task[i]]
    print(ans)

if __name__ == '__main__':
    main()