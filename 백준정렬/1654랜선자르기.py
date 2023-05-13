import sys
input = sys.stdin.readline

K, N = map(int, input().split())    # 전선 개수 , 필요전선 개수
arr = [int(input()) for _ in range(K)]
start , end = 1, max(arr)   # 첫 구간 설정 >> 1~배열의 최대까지
while start <= end: # 이진분법 돌릴 범위
    cnt = 0 # 자른 전선 개수 초기화
    midd = (start+end) // 2 # 중간값 설정
    for i in arr:   # 배열의 전선길이 하나씩 빼서 자를 수 있는 전선 찾아내기
        cnt += i // midd
        # print(count)
    if cnt >= N:        # 전선 개수가 필요개수보다 크다면 크기를 더 키워서 줄여보기
        start = midd +1 

    else:       # 작다면 크기를 줄여서 찾아보기
        end = midd -1
print(end)



    
    
