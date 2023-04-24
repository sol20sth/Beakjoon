
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
cnt = 1
while b!=a:
  cnt += 1
  tmp = b
  if b%2 == 0:
    b = b//2
  elif b%10 == 1:
    b = b//10
  # print(b)
  if b == tmp :
    print(-1)
    break
if b == a:
  print(cnt)
    
  