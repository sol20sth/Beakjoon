import sys
input = sys.stdin.readline
# 행의 최대길이를 찾아서 그 값들을 차례로 딕셔너리에 넣어서 자리에 따라서 
# 값을 집어 넣어봤지만 같은 알파벳들이 다른자리에 들어간 경우 크기에 따른 최대값 비교가 불가능
stack = [x for x in range(1, 10)]
dic = {}
dic['0'] = ''
print(stack)
n = int(input())

wd = [list(input())[:-1][::-1] for _ in range(n)]
print(wd)
wdlen = [0] * n
for i in range(len(wd)):
  wdlen[i] = len(wd[i])
mxlen = max(wdlen)

for i in range(n):
  [wd[i].append('0') for _ in range(mxlen-wdlen[i])]
print(wd)

while mxlen:
  for i in range(n-1, -1, -1):
    if mxlen == wdlen[i] and wd[i][mxlen-1] not in dic.values():
      dic[wd[i][mxlen-1]] = stack.pop()
      wdlen[i] -= 1
      print(stack, dic)
  mxlen -= 1
print(dic)
fini = ['' for _ in range(n)]
for i in range(n):
  for j in range(n-1, -1, -1):
    fini[i] += dic[wd[i][j]]
print(fini)



#########################################################################
import sys
input = sys.stdin.readline

stack = [x for x in range(10)]  #나중에 곱해줄 0~9숫자
# print(stack)
n = int(input())
wd = [input()[:-1] for _ in range(n)] # 받는 알파벳
# print(wd, wdlen)
ans = [0] * 26  # 알파벳들별로 가지는 숫자들의 합을 받을 리스트
for i in range(n):  # 행 우선탐색
  tmp = len(wd[i])-1  # 각 리스트의 각 알파벳들의 숫자자리 잡기위한 변수
  for j in wd[i]:   # 열탐색 
    ans[ord(j)-65] += (10**tmp)   # 각 알파벳들을 숫자로 받아 A 를 0번쨰 인덱스로 설정후
                                  # 각자리의 값들을 더해줌 
                                  # 중복값들 신경쓰지 않고 처리가능
    tmp -= 1
ans.sort()                        # 받은 값들 정렬
total = 0
for i in range(10):               # 총 10개의 알파벳과 숫자들만 필요하므로 앞에 16개는 무조건 0이나온다 
  total += ans[i+16] * stack[i]   # 그래서 17번째부터 스택의 앞의 작은 숫자와 곱한 것들을 더해주어서 토탈에 넣기
print(total)



# https://lab.ssafy.com/s09/python/web