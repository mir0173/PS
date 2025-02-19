from sys import stdin
input = stdin.readline
t = int(input())
results = []

def re(start, a, b, c, n, m, list1, list2):
    for i in range(start, n):
        a[i + 1] = min(b[i] + 1, c[i] + 1)

        if list1[i] + list2[i] <= m:
            a[i + 1] = min(a[i + 1], a[i] + 1)

        if list1[i - 1] + list1[i] <= m and list2[i - 1] + list2[i] <= m:
            a[i + 1] = min(a[i + 1], a[i - 1] + 2)

        if i < n - 1:
            b[i + 1], c[i + 1] = a[i + 1] + 1, a[i + 1] + 1
            if list1[i + 1] + list1[i] <= m:
                b[i + 1] = min(b[i + 1], c[i] + 1)  
            if list2[i + 1] + list2[i] <= m:
                c[i + 1] = min(c[i + 1], b[i] + 1)

    return a, b, c

def main():
    for _ in range(t):
        n, m = map(int, input().split())
        list1 = list(map(int, input().split()))
        list2 = list(map(int, input().split()))
        a, b, c = re(0, [0 for _ in range(n + 1)], [1] + [0 for _ in range(n)], [1] + [0 for _ in range(n)], n, m, list1, list2)
        result = a[n]
        if n > 1:
            if list1[0] + list1[n - 1] <= m:
                a[1], b[1] = 1, 2
                c[1] = 1 if list2[0] + list2[1] <= m else 2
                a, b, c = re(1, a, b, c, n, m, list1, list2)
                result = min(result, c[n - 1] + 1)

            if list2[0] + list2[n - 1] <= m:
                a[1], c[1] = 1, 2
                b[1] = 1 if list1[0] + list1[1] <= m else 2
                a, b, c = re(1, a, b, c, n, m, list1, list2)
                result = min(result, b[n - 1] + 1)

            if list1[0] + list1[n - 1] <= m and list2[0] + list2[n - 1] <= m:
                a[1], b[1], c[1] = 0, 1, 1
                a, b, c = re(1, a, b, c, n, m, list1, list2)
                result = min(result, a[n - 1] + 2)
    
        results.append(result)
    
    for answer in results:
        print(str(answer))

if "__main__" == __name__:
    main()