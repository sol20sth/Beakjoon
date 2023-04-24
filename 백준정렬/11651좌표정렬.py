import sys
input = sys.stdin.readline

T = int(input())

list_all = [list(map(int, input().split())) for _ in range(T)]  # 2차원 배열로 입력받기

# print(list_all)

list_all.sort(key=lambda x:(x[1] ,x[0])) # 리스트의 인덱스 1,0번순으로 정렬

for i in range(T):
    
    print(*list_all[i])
