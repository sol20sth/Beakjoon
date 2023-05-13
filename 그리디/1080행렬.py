# def chge(i, j):
#   for a in range(i,i+3):    # 3*3 모두 변경
#     for b in range(j,j+3):
#       if list1[a][b] == '1': # 1아니면 0 , 0이아니면 1로 변경
#         list1[a][b] = '0'
#       else:
#         list1[a][b] = '1'

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# list1 = [list(input()) for _ in range(n)] # 바꾸기전의 행렬
# list2 = [list(input()) for _ in range(n)] # 만들어야 할 행렬
# cnt = 0   # 바꾼 횟수
# for i in range(n-2):  # 3*3 을 바꿔야 함으로 행렬 -2 까지 반복
#   for j in range(m-2):
#     if list1[i][j] != list2[i][j]: # 만약 값이 다르다면
#       chge(i, j)  # 바꿔주는 함수 실행
#       cnt += 1  # 카운트 +1
# if list1 != list2:  # 만약 다 돌았는데도 같지 않으면 
#   cnt = -1  # -1 처리
# print(cnt)
