from sys import stdin
input = stdin.readline
num = int(input())
answer = []

def get_seat(row):
    cnum = 0
    for char in row:
        cnum *= 2
        if char == "x":
            cnum |= 1
    return cnum

def one_num(n):
    key, ans = 1, 0
    while key <= n:
        if key & n == key:
            ans += 1
        key *= 2
    return ans

def check(n):
    key = 3
    while key <= n:
        if key & n == key:
            return True
        key *= 2
    return False

def main():
    for _ in range(num):
        r, c = map(int, input().split())
        dp = [[0] * (2 ** c) for _ in range(r)]
        mat = [input().rstrip() for _ in range(r)]
        now = 0
    
        for r_index in range(r):
            possi = get_seat(mat[r_index])
    
            for c_index in range(2 ** c):
                if not (c_index & possi) and not check(c_index):
                    ones = one_num(c_index)
    
                    if not r_index:
                        dp[0][c_index] = ones
                    else:
                        max_val = ones
    
                        for c0_index in range(2 ** c):
                            if not (c0_index & now):
                                new_seat = c0_index | c_index
                                if not check(new_seat):
                                    tmp = ones + dp[r_index - 1][c0_index]
                                    if tmp > max_val:
                                        max_val = tmp
                        dp[r_index][c_index] = max_val
            now = possi
        answer.append(max(dp[-1]))

    for i in range(num):
        print(answer[i])
        
if __name__ == '__main__':
    main()