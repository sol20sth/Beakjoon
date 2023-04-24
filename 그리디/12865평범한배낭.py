import sys
input = sys.stdin.readline

n , k = map(int, input().split())
li = [[0,0]]
arr = [[0] * (k+1) for _ in range(n+1)]
for _ in range(n):
  li.append(list(map(int, input().split())))

for i in range(1,n+1):
  for j in range(1, k+1):
    we = li[i][0]
    va = li[i][1]
    if we > j:
      arr[i][j] = arr[i-1][j]
    else:
      arr[i][j] = max(va + arr[i-1][j-we], arr[i-1][j])
print(arr[n][k])

