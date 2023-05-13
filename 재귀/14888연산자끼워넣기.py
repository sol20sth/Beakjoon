import sys
input = sys.stdin.readline
from itertools import permutations # 순열 
n = int(input())
num2 = list(map(int, input().split()))[::-1]  # 뒤에서부터 뺴내기 위해 돌리기
a, b, c, d = map(int, input().split())  # 기호들 숫자 받기
sign = ''
sign += a*'+' + b*'-' + c*'*' + d*'/'   # 기호들 문자열로 모으기
sign = list(sign) # 리스트로 바꾸기
sign = list(permutations(sign, len(sign)))  # 기호들의 순열 모으기
mx, mi = -1000000001, 1000000001    # 최대 최소값 설정
for j in range(len(sign)):    # 기호 순열들 모두 탐색
  num = num2[::]    # 숫자들 계속 새로받기
  for i in range(len(sign[j])):   # 기호 개수만큼 탐색
    x1, x2 = num.pop(), num.pop()   # 2개빼서 계산
    if sign[j][i] == '+':   # +일때 더하기
      num.append(x1+x2)
    elif sign[j][i] == '-':   # -일떄 뺴기
      num.append(x1-x2)
    elif sign[j][i] == '*': # * 일떄 곱하기
      num.append(x1*x2)
    elif sign[j][i] == '/':   # / 일때 둘중하나가 음수이면 양의수에서 몫에 -1곱해주기
      if x1 * x2 < 0:
        num.append((abs(x1)//abs(x2))*(-1))
      else:
        num.append(abs(x1)//abs(x2))
    # print(num)
  if mx < num[0]: # 최대 최소값 계속 확인
    mx = num[0]
  if mi > num[0]:
    mi = num[0]
print(mx)
print(mi)