def check(idx, sm):
  global cnt 
  sm += arr[idx]
  if sm == b:
    cnt += 1
  if idx == a-1:
    return
  check(idx+1, sm)
  sm -= arr[idx]
  check(idx+1, sm)

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
check(0, 0)
print(cnt)