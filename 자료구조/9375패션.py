import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
  n = int(input())
  dic = {}
  ans = 1
  for i in range(n):
    a, b = map(str, input().split())
    if b in dic.keys():
      dic[b] += 1
    else:
      dic[b] = 1
  for i in dic.values():
    ans *= (i+1)
  print(ans-1)