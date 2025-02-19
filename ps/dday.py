from datetime import *
day = list(map(int, input().split()))
day2 = list(map(int, input().split()))

def main():
    if day[0] + 1000 < day2[0]:
        print("gg")
    elif day[0] + 1000 == day2[0] and (day[1], day[2]) <= (day2[1], day2[2]):
        print("gg")
    else:
        today = date(*day)
        dday = date(*day2)
        print("D-"+str(dday.toordinal() - today.toordinal()))

if __name__ == '__main__':
    main()