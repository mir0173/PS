#1069
from sys import stdin
input = stdin.readline
def main():
  x, y, d, t = map(int, input().split())
  dist = (x ** 2 + y ** 2) ** 0.5
  
  if d / t <= 1 : print(dist); return
  
  tmp = dist // d * t + min(dist % d, t + (d - dist % d))
  ans = min(tmp, max(2 * t, dist // d * t + t))
  print(ans)

if __name__ == '__main__':
  main()