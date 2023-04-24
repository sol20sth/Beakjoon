import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
stack1 ,stack2= [], []
for i in arr:
  if i % 10 == 0:
    stack1.append(i//10 -1)  # 10의배수
stack1.sort()
for i in arr:
  if i % 10 != 0:
    stack2.append(i//10)    # 10의 배수아닐때
stack2.sort()
ans = 0
if sum(stack1) <= m:    # 자를 횟수가 10의배수를 모두 자를수 있을떄
  ans = len(stack1) + sum(stack1)
  m -= sum(stack1)
  if sum(stack2) <= m:
    ans += sum(stack2)
  else:
    ans += m
else:       # 10의 배수를 모두 자를 수 없을떄
  for i in range(len(stack1)):
    if m > stack1[i]:
      ans += stack1[i]+1
      m -= stack1[i]
    elif m == stack1[i]:
      ans += stack1[i] + 1
      break
    else:
      ans += m
      break
print(ans)

