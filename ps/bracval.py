#2504
from sys import stdin
input = stdin.readline
def main():
    brac, key, answer, tmp= input().rstrip(), [], 0, 1
    for i in range(len(brac)):
        if brac[i] == '(': key.append(brac[i]); tmp *= 2
        elif brac[i] == '[': key.append(brac[i]); tmp *= 3
        elif brac[i] == ")":
            if not key or key[-1] == "[": answer = 0; break
            if brac[i-1] == "(": answer += tmp
            key.pop()
            tmp //= 2
        else:
            if not key or key[-1] == "(": answer = 0; break
            if brac[i-1] =='[': answer += tmp
            key.pop()
            tmp //= 3
    print(0 if key else answer)

if __name__ == '__main__':
    main()