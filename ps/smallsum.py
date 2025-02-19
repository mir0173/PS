from sys import stdin
input = stdin.readline

def main():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    left, right = 0,0
    sum = 0
    ans = 1e5

    while True:
        if sum >= s:
            ans = min(ans, right-left)
            sum -= nums[left]
            left += 1
        elif right == n:
            break
        else:
            sum += nums[right]
            right += 1

    print(0 if ans == 1e5 else ans)

if __name__ == '__main__':
    main()
