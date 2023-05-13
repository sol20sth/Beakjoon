arr = [int(input()) for _ in range(9)]
# print(arr)
sm = sum(arr)
stack = []
for i in range(8):
  for j in range(i+1, 9):
    tmp = arr[i] + arr[j]
    if sm - tmp == 100:
      stack.append([i, j])
      break
stack2 = []
# print(stack)
for i in range(9):
  if i != stack[0][0] and i != stack[0][1]:
      stack2.append(arr[i])
stack2.sort()
# print(stack2)
for i in stack2:
  print(i)