
import sys
input = sys.stdin.readline
n = int(input())
stack = []
for i in range(n):
  stack.append(list(map(int, input().split())))
stack.sort(key=lambda x : (x[1], x[0]))

# print(stack)
cnt , end = 0, 0

for i,j in stack:
  if i >= end:
    cnt += 1
    end = j
print(cnt)