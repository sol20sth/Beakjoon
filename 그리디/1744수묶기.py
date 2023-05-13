'''
n 수열

양수 >> 1을 제외한 모든 수를 묶는다
음수 개수 2의배수 >> 음수 모두 묶는다
음수 개수 홀수 >> 절대값이 가장 작은 수를 제외한 모든 수를 묶는다.
'''
import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
cnt = 0
mi_mi = -1001
arr.sort()
stack1 , stack2 = [], []
total = 0
tf = False
for i in arr:
  if i < 0 :
    cnt += 1
    stack2.append(i)
  elif i == 1:
    total += 1
  elif i == 0:
    tf = True
  else:
    stack1.append(i)
stack1.sort(reverse=True)
for i in range(len(stack1)//2):
  total += stack1[2*i] * stack1[2*i + 1]
if len(stack1) % 2 == 1:
  total += stack1[-1]
for i in range(len(stack2)//2):
  total += stack2[i*2] * stack2[i*2 + 1]
if len(stack2) % 2 == 1 and tf == False:
  total += stack2[-1]
print(total)