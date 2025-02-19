import math
a, b = map(int, input().split())
List = []
for _ in range(a):
    List.append(list(map(str, list(input()))))

def main():
    answer = -1
    for i1 in range(a):
        for j1 in range(b):
            for i2 in range(-a, a):
                for j2 in range(-b, b):
                    string = ""
                    i, j = i1, j1
                    if i2 == 0 and j2 == 0: continue
                    while -1 < i < a and -1 < j < b:
                        string += List[i][j]
                        answer = max(answer, int(string)) if math.sqrt(int(string)).is_integer() else answer
                        i += i2
                        j += j2
    print(answer)

if __name__ == '__main__':
    main()