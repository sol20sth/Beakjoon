import sys

input = sys.stdin.readline  # 한줄씩 입력받기
T = int(input())
arr = []        #빈배열 생성
for i in range(T):
    arr.append(input().split()) #입력받은 값 배열에 추가
# 배열정렬 arr[0]>> 나이순으로 정렬    
arr.sort(key=lambda x: int(x[0]))   
for j in range(T):  # 나이 이름순으로 T번 프린트 
    print(arr[j][0], arr[j][1])