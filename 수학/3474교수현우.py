import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  a = int(input())
  cnt = 0
  while a//5 !=0:
    a = a//5
    cnt += a
  print(cnt)