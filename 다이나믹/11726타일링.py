
  
n = int(input())
stack = [0] * 10002
for i in range(1, n+1):
  if i == 1:
    stack[i] = 1
  elif i == 2:
    stack[i] = 2
  else: 
    stack[i] = stack[i-1] + stack[i-2]
  # print(stack)
print(stack[n]%10007)
