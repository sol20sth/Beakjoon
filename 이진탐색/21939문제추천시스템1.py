'''
recommend : x가 1인경우 가장어려운 문제, 같으면 큰문제
                -1인 경우 가장 쉬운문제 같으면 작은 것
add P L : L난이도 문제번호P
solved P : P를 제거
하나이상있을때 주어짐

N : 문제의 개수
P L 공백으로 주어짐 
M : 명령문개수
M개 명령문
'''
def recommend(x):

  if x == 1:
    i = len(arr)-1
    print(i, arr)
    while arr[i][2]: 
      arr.pop(i)
      i -= 1
    print(arr[-1][1])
  else:
    i = 0
    while not arr[i][2]: 
      arr.pop(i)
      i += 1
    print(arr[0][1])

def add(P, L):
  arr.append([L,P,0])

def solved(P):
  for case in arr:
    if case[1] == P:
      case[2] = 1
      return
    else:
      continue


import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
  P, L = map(int, input().split())
  arr.append([L,P,0])
print(arr)
M = int(input())

for _ in range(M):
  com, *num = map(str, input().split())
  # print(com, num)
  if com == 'add':
    add(int(num[0]), int(num[1]))
  elif com == 'recommend':
    recommend(int(num[0]))
  elif com == 'solved':
    solved(int(num[0]))
    
    
##########################################

# from heapq import heappush, heappop
# import sys
# input = sys.stdin.readline

# n = int(input())
# min_h, max_h = [], []
# d = {}
# for _ in range(n):
#     p, l = map(int, input().split())
#     heappush(min_h, [l, p])
#     heappush(max_h, [-l, -p])
#     d[p] = True
# M = int(input())
# for _ in range(M):
#     command = input().split()
#     if command[0] == 'recommend':
#         if command[1] == '1':
#             while not d[-max_h[0][1]]:
#                 print(max_h, d)
#                 heappop(max_h)
#             print(max_h, d)
#             print(-max_h[0][1])
#         else:
#             while not d[min_h[0][1]]:
#                 heappop(min_h)
#             print(min_h[0][1])
#     elif command[0] == 'add':
#         p, l = int(command[1]), int(command[2])
#         while not d[-max_h[0][1]]:
#             heappop(max_h)
#         while not d[min_h[0][1]]:
#             heappop(min_h)
#         d[p] = True
#         heappush(max_h, [-l, -p])
#         heappush(min_h, [l, p])
#     else:
#         d[int(command[1])] = False