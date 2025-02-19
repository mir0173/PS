a, b = map(int, input().split())
list1 = []
for _ in range(a):
    list1.append(list(map(int, list(input()))))
list2 = []
for _ in range(a):
    list2.append(list(map(int, list(input()))))


def reverse(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            list1[i][j] = 1 if list1[i][j] == 0 else 0



def main():
    ans = 0
    if (a < 3 or b < 3) and list1 != list2:
        ans = -1
    else:
        for k in range(a - 2):
            for l in range(b - 2):
                if list1[k][l] != list2[k][l]:
                    ans += 1
                    reverse(k, l)

    if ans != -1 and list1 != list2:
        ans = -1

    print(ans)


if __name__ == '__main__':
    main()