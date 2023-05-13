x, y = map(int, input().split())
n = int(input())
visited = [[[0,0]for _ in range(x)] for _ in range(y)]
# print(visited)
for _ in range(n):
  a, b = map(int, input().split())
  
  for i in range(y):
    for j in range(x):
      if j < a:
        visited[i][j][1] -= 1
      else:
        break
      
  for i in range(x):
    for j in range(y):
      if j < b:
        visited[j][i][0] -= 1
      else:
        break
  print(visited)
dict = {}
for i in range(y):
  for j in range(x):
    if visited[i][j] in dict.keys():
      dict[visited[i][j]] += 1
    else:
      dict[visited[i][j]] = 1
print(max(max(dict.values())))

#################################################
import sys
input = sys.stdin.readline
m,n = map(int, input().split())
num = int(input())
lnm = [0] * (m+1)
lnn = [0] * (n+1)
for i in range(num):
    a, b = map(int, input().split())
    if a == 1:
        lnm[b] = 1
    else:
        lnn[b] = 1
mxm, mxn = 0, 0
mm, nn = 0, 0
for i in range(m+1):
    if lnm[i] == 1 or i == m:
        if mm < mxm:
            mm = mxm
        mxm = 1
    else: 
        mxm += 1
for i in range(n+1):
    if lnn[i] == 1 or i == n:
        if nn < mxn:
            nn = mxn
        mxn = 1
    else: 
        mxn += 1
# print(nn, mm)
print(nn*mm)