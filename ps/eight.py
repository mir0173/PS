A, B = map(str, input().split(' '))

def main():
    ans = 0
    if len(A) != len(B):
        print(0)

    else:
        for i in range(len(A)):
            if A[i] == B[i]:
                if A[i] == '8':
                    ans += 1
            else:
                break
        print(ans)

if __name__ == '__main__':
    main()