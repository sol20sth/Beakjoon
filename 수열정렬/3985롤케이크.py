cake = int(input())
peo = int(input())
ca = [0] * (cake+1)
num = 1
mxx = 0
for _ in range(peo):
  a, b = map(int, input().split())
  for i in range(a, b+1):
    if ca[i] == 0:
      ca[i] = num
  if mxx < b-a:
    mxx = b-a
    tmp = num
  num += 1
mx= 0
stack = [0] * (peo+1)
for i in ca:
  if i != 0:
    stack[i] += 1
# print(stack)
mxidx = 0
for i in range(peo, 0, -1):
  if stack[i] >= mx:
    mx = stack[i]
    mxidx = i

print(tmp)
print(mxidx)