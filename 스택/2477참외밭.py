import sys
input = sys.stdin.readline

T = int(input())
stack = list()
for _ in range(6):
  stack.append(list(map(int, input().split())))
# print(stack)
mx1, mx2 = 0, 0
mxidx1, mxidx2  =0, 0
for i in range(len(stack)):
  if stack[i][0] == 1 or stack[i][0] == 2:
    if stack[i][1] > mx1:
      mx1 = stack[i][1]
      mxidx1 = i
  elif stack[i][0] == 3 or stack[i][0] == 4:
    if stack[i][1] > mx2:
      mx2 = stack[i][1]
      mxidx2 = i
# print(stack)
# print(mx1, mx2, mxidx1, mxidx2)
mi1 = stack[(mxidx1-1)%6][1] - stack[(mxidx1+1)%6][1]
mi2 = stack[(mxidx2-1)%6][1] - stack[(mxidx2+1)%6][1]

ans = (mx1 * mx2) - abs(mi1*mi2)
print(ans*T)
  