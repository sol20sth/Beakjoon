import sys
input = sys.stdin.readline
n= int(input())
arr = list(input())
stack = []
for i in range(len(arr)-1):
  if arr[i] == '(' and arr[i+1]==')':
    stack.append([i,i+1])
# print(stack)
for x in range(len(stack)):
  i, j = stack[x][0], stack[x][1]
  s, e = i, j
  for k in range(1, i+1):
    if arr[i-k] == '(' and arr[j+k] ==')':
      s , e = i-k, j+k
      stack[x][0] , stack[x][1] = s,e
    else:
      break
# print(stack)
mx = 0
s, e = stack[0][0], stack[0][1]
for i in range(len(stack)-1):
  if stack[i][1] +1 == stack[i+1][0]:
    s, e = s, stack[i+1][1]
  else:
    mx = max(e-s+1, mx)
    s, e = stack[i+1][0], stack[i+1][1]
  if i == len(stack)-2:
    mx = max(e-s+1, mx)
    break
print(mx)