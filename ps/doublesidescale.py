#2629
from sys import stdin
input = stdin.readline

n = int(input())
w_list = list(map(int, input().split()))
m = int(input())
ex_list = list(map(int, input().split()))

def main():
    pos_w_set = {0}
    for weight in w_list:
        new_weights = set()
        for w in pos_w_set:
            new_weights.add(w + weight)
            new_weights.add(abs(w - weight))
        pos_w_set |= new_weights

    print(*["Y" if x in pos_w_set else "N" for x in ex_list])

if __name__ == '__main__':
    main()
