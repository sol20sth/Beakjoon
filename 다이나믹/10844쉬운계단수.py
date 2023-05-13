def f(a):
  global cnt
  if a == n:
    return
  else:
    cnt = cnt*2 - a
    f(a+1)


import sys
imput = sys.stdin.readline

n = int(input())

cnt = 9
f(1)
print(cnt)