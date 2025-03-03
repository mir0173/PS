# 1071
from sys import stdin
input = stdin.readline
from collections import Counter

n = length = int(input())
List = list(map(int, input().split()))
count = Counter(List)
srt = sorted(count)
ans = []

def insert(index):
    global length
    while count[index]:
        ans.append(index)
        count[index] -= 1
        length -= 1

def main():
    global length
    while length > 0:
        for i in range(len(srt)):
            boolean, key = True, srt[i]
            if count[key]:
                if key + 1 in srt and count[key + 1]:
                    for j in srt[i + 1:]:
                        if key + 2 <= j and count[j]:
                            insert(key)
                            ans.append(j)
                            count[j] -= 1
                            length -= 1
                            boolean = False
                            break
                    if boolean:
                        ans.append(int(key + 1))
                        count[key + 1] -= 1
                        length -= 1
                else:
                    insert(key)
    print(*ans)

if __name__ == '__main__':
    main()