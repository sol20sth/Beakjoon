import sys
input = sys.stdin.readline

n = int(input())
visited = [[0]*100 for _ in range(100)] 
for i in range(n):
  a, b = map(int, input().split())
  for i in range(a, a+10):
    for j in range(b, b+10):
      visited[i][j] = 1
cnt = 0
for i in range(100):
  for j in range(100):
    if visited[i][j] == 1:
      cnt += 1  
print(cnt)