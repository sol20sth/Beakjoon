def f():
    cnt = 0
    for i in range(5):
        for j in range(5):
            visited[di[numarr[i][j]][0]][di[numarr[i][j]][1]] = 1
            cnt += 1
            bingo = 0
            
            if cnt > 10:
                for k in range(5):
                    if sum(visited[k]) == 5:
                        bingo += 1
                    if sum(l[k] for l in visited) == 5:
                        bingo += 1
                if visited[0][0]+visited[1][1]+visited[2][2]+visited[3][3]+visited[4][4] == 5:
                    bingo += 1
                if visited[0][4]+visited[1][3]+visited[2][2]+visited[3][1]+visited[4][0] == 5:
                    bingo += 1
                # print(visited)
                if bingo >= 3:
                    return cnt

import sys 
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(5)]
di = {}
for i in range(5):
    for j in range(5):
        di[arr[i][j]] = (i,j)
numarr = [list(map(int, input().split()))for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
print(f())
# print(visited)
# print(numarr)
# print(di)
##################
# import sys
# input = sys.stdin.readline

# # 숫자들의 위치 기록
# board = dict()
# check = [[0]*5 for i in range(5)]
# for i in range(5):
#     a = list(map(int,input().split()))
#     for j in range(5):
#         board[a[j]] = (i,j)

# tick = 0
# for _ in range(5):
#     a = list(map(int,input().split()))
#     for i in range(5):
#         tick += 1
        
#         # 불린 숫자가 보드에 있을 경우
#         if a[i] in board:
#             # 딕셔너리를 이용해 기록
#             check[board[a[i]][0]][board[a[i]][1]] = 1
            
#             # 빙고 세주기
#             bingo = 0
#             for j in range(5):
#                 if sum(check[j]) == 5:
#                     bingo+=1
#                 if sum([k[j] for k in check]) == 5:
#                     bingo+=1
#             if check[0][4]+check[1][3]+check[2][2]+check[3][1]+check[4][0] == 5:
#                 bingo+=1
#             if check[0][0]+check[1][1]+check[2][2]+check[3][3]+check[4][4] == 5:
#                 bingo+=1
                
#             if bingo >= 3:
#                 print(tick)
#                 sys.exit()