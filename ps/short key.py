#1283
n = int(input())

def main():
    List = []
    for _ in range(n):
        words = list(input().split())
    
        key = False
        for i in range(len(words)):
            if words[i][0].upper() not in List:
                List.append(words[i][0].upper())
                key = True
                words[i] = '[' + words[i][0] + ']' + words[i][1:]
                print(' '.join(words))
                break
    
        if not key:
            for i in range(len(words)):
                check = False
                for j in range(len(words[i])):
                    if words[i][j].upper() not in List:
                        List.append(words[i][j].upper())
                        key = True
                        check = True
                        words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j + 1:]
                        print(' '.join(words))
                        break
                if check: break
    
        if not key:
            print(' '.join(words))

if __name__ == '__main__':
    main()