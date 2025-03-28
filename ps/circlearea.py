#10000
from sys import stdin
input = stdin.readline
import heapq

def main():
    n = int(input())
    arr = []
    key, ans = [], 1

    for _ in range(n):
        x, r = map(int, input().split())
        arr.append((x + r, 2 * r))
    arr.sort()

    for i in range(n):
        end, dist = arr[i]
        start, trig, last = end - dist, False, end
        while key:
            a, b = heapq.heappop(key)
            a = -a
            if a <= start:
                heapq.heappush(key, (-a, b))
                break
            if a != last and a - b >= start: continue
            if a - b >= start: last = a - b
            if last == start: trig = True
        ans += 1
        if trig: ans += 1
        heapq.heappush(key, (-end, dist))
    print(ans)

if __name__ == '__main__':
    main()