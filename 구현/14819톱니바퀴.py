import sys
from collections import deque
input = sys.stdin.readline
lis = [deque(list(map(int,input().rstrip()))) for _ in range(4)]
# 톱니바퀴의 ns 리스트
k = int(input())
# 회전 횟수
target = [list(map(int, input().split())) for _ in range(k)]
# 회전 톱니, 방향 받는 리스트
for i in range(len(target)):
    n = target[i][0] - 1 # 톱니 번호 인덱스로 바꾸기
    v = target[i][1]  # 바향 변후
    tmp = []  # 톱니는 한번에 움직인다고 생각해야 하기 때문에 현재 상태의 톱니 좌우를 저장할 리스트
    for l in range(4): # 4개의 톱니 좌우 극 저장하기
        tmp.append([lis[l][2], lis[l][6]])
    # print(tmp)
    if n != 3: # 우측을 볼 필요 없는경우 제외
        for j in range(n, 3): # 3번 톱니까지만 반복
            if tmp[j][0] != tmp[j+1][1]: # 좌우가 같지 않을떄
                if (n-j)%2 == 0: # 현재 톱니에서 짝수번쨰에 있는 톱니이면
                    lis[j+1].rotate(-v) # 한칸 오른쪽은 반대방향으로 돌리기
                else: # 홀수번쨰라면
                    lis[j+1].rotate(v) # 한칸 오른쪽은 첫방향과 같은방향으로 돌리기 
            else: # 극이 같으면 돌아가지 않음
                break
    if n != 0:  # 왼쪽 비교 >> 0번째 아닐때 
        for j in range(n, 0, -1): # 현재부터 좌로 이동하며 반복
            # print(j, tmp[j][1], tmp[[j-1][0]])
            if tmp[j][1] != tmp[j-1][0]:  # 현재 톱니 왼쪽과 왼쪽톱니 오른쪽의 극이 다르면
                if (n-j)%2 == 0: # 짝수번째라면
                    lis[j-1].rotate(-v) # 왼쪼은 홀수라 생각해서 반대방향
                else: # 홀수라면
                    lis[j-1].rotate(v) # 왼쪽은 짝수라 생각
            else: # 다르면 종료
                break
    lis[n].rotate(v) # 기준 돌리는 톱니도 돌려주기

sum = 0 # 1~4번 톱니까지 12시방향 방향 찾아서 1이면 각각 1, 2, 4, 8 더해주기
if lis[0][0] == 1:
    sum += 1
if lis[1][0] == 1:
    sum += 2
if lis[2][0] == 1:
    sum += 4
if lis[3][0] == 1:
    sum += 8
print(sum)