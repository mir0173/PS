from sys import stdin
input = stdin.readline

def seq(n, List):
    if n == 1:
        return 'A'
    if n == 2:
        return List[0] if List[0] == List[1] else 'A'

    key = 0 if List[0] == List[1] else (List[1] - List[2]) // (List[0] - List[1])
    key2 = List[1] - List[0] * key
    for i in range(n - 1):
        next = List[i] * key + key2
        if List[i + 1] != next:
            return 'B'
    return int(List[- 1] * key + key2)


def main():
    n = int(input())
    List = list(map(int, input().split()))
    print(seq(n, List))

if __name__ == '__main__':
    main()