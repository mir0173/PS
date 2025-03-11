#1149
n = int(input())
List = [0] * n

for i in range(n):
    List[i] = list(map(int, input().split()))

for i in range(1, n):
    List[i][0] = min(List[i - 1][1], List[i - 1][2]) + List[i][0]
    List[i][1] = min(List[i - 1][0], List[i - 1][2]) + List[i][1]
    List[i][2] = min(List[i - 1][0], List[i - 1][1]) + List[i][2]
print(min(List[n - 1][0], List[n - 1][1], List[n - 1][2]))