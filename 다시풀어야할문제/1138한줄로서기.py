import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr0 = [0]*n
for i in range(n):
  tmp = 0
  # print(arr0)
  for j in range(n):
    if tmp == arr[i] and arr0[j]==0:
      arr0[j] = i+1
      break

    elif arr0[j] != 0:
      continue
    elif arr0[j] == 0:
      tmp += 1
print(*arr0)      



