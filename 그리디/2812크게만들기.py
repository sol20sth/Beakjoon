n, m = map(int, input().split())
num = list(input())

stack = []
tmpM = m
while tmpM != 0 :
  for i in range(n):
    for j in range(i+1, i+1+tmpM):
      if num[i] < num[j]:
        stack.append(num[i])
        tmpM -= 1
        break
print(stack)
for i in stack:
  num.remove(i)
print("".join(map(str, num)))

n, m = map(int, input().split())
num = list(input())
stack = [] # 지워지지 않는 숫자들 모으는 리스트

for i in range(n): # 숫자 앞자리부터 탐색 >> 앞자리에서부터 작은 수 없애기
  while stack and m > 0 and stack[-1] < num[i]: # 스택이 채워져 있고, 더 제거해야 하며, 
    # 스택의 뒤에서부터 현재 숫자보다 작은 숫자 지우기 크거나 작은 숫자 나올 때까지
    # 지울떄마다 지워야 하는 숫자 -1 해주기 
    stack.pop()
    m -= 1
  stack.append(num[i]) # 스택에서 불필요한 숫자 지웠다면 스택에 숫자 넣기
if not stack: # 스택이 비어있으면
  print("".join(map(str, stack))) # 스택숫자 붙여서 출력
else: # 비어있지 않으면
  print("".join(map(str, stack[:len(stack)-m]))) # 뒤에 m개만큼 빼고 출력