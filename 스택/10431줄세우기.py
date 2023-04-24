import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  arr = list(map(int, input().split()))
  cnt = 0
  for i in range(1, len(arr)-1):
    for j in range(i+1, len(arr)):
      if arr[i] > arr[j]:
        cnt += 1
  print(f'{arr[0]} {cnt}')