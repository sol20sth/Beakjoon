'''
Hamming Distace : 길이가 같은 DNA 있을떄 다른 개수


'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = [list(map(str, input())) for _ in range(n)]
stack = ''
for i in range(m):
  li = [['A',0], ['C',0], ['G',0], ['T',0]]
  mx = 0
  for j in range(n):
    if arr[j][i] == 'A':
      li[0][1] += 1
      mx = max(li[0][1], mx)
    elif arr[j][i] == 'C':
      li[1][1] += 1
      mx = max(li[1][1], mx)
    elif arr[j][i] == 'G':
      li[2][1] += 1
      mx = max(li[2][1], mx)
    else:
      li[3][1] += 1
      mx = max(li[3][1], mx)
  for k in range(4):
    if li[k][1] == mx :
      stack += li[k][0]
      break
print(stack)
tmp = 0
for i in range(n):
  for j in range(m):
    if arr[i][j] != stack[j]:
      tmp += 1
print(tmp)