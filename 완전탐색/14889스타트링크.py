def f(start, cnt):

  if cnt == n//2 :
    stack2.append(''.join(map(str, stack)))
    return
  for k in range(start, n):
    stack.append(k)
    f(start+1, cnt + 1)
    stack.pop()

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

mi = 1000000000
stack  =  []
stack2 = []
f(0, 0)

for i in stack2:
  start, link = 0, 0
  for j in range(n):
    for k in range(n):
      if str(j) in i and str(k) in i and j != k:
        start += arr[j][k]
      elif str(j) not in i and str(k) not in i and j != k:
        link += arr[j][k]
  mi = min(mi, abs(start-link))
print(mi)