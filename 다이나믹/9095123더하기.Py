def f(a, n):
  global cnt 
  if a == n:
    cnt +=1 
    return
  if a > n :
    return
  f(a+1, n)
  f(a+2, n)
  f(a+3, n)
  
import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
  n = int(input())
  cnt = 0
  f(0,n)
  
  print(cnt)