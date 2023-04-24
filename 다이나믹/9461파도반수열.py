

T = int(input())
arr = [int(input()) for _ in range(T)]

stack = [0] * (max(arr)+1)
stack[1] = 1
stack[2] = 1
for i in range(3, len(stack)):
  stack[i] = stack[i-2] + stack[i-3]
  
for i in arr:
  print(stack[i])