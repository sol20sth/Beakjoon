# for i in range(M):  
#     if comp[i] in numlist:       
#         print('1')
#         continue
#     else:
#         print('0')
N = int(input())
numlist = list(map(int,input().split()))    #  숫자들을 배열로 받는다.
M = int(input())
comp = list(map(int,input().split()))   # 비교할 숫자를 배열로 받는다.
numlist.sort() # 기준 배열을 정렬시킨다.
for i in comp:  # 비교할 배열에 있는 수들을 빼낸다
    final = 0   
    start, end = 0, N-1     # 초기값, 끝값 == 배열인덱스 끝값, 정답을 설정
    while start <= end:  # 이진분법 >>>> 시작점이 끝점보다 커질때까지 반복문돌리겠다. 비교할 구간을 계속 잘라내서 
        mid = (start + end) // 2    # 가까워진다.
        if numlist[mid] < i :   # 전체구간에서 numlist 중간값이 i 보다 작으면 i는 오른쪽에 있을 것이라 판단해서
            start = mid + 1     # 구간을 오른쪽으로 옮기기 위한 작업인 시작점을 mid +1로 옮긴다
        elif numlist[mid] > i : # 클때는 반대로 왼쪽이라 생각해서
            end = mid - 1       # 끝점을 mid-1로 옮긴다
        else:
            final = 1       # 둘다 아닐시 == 같을때 == 포함 될때 
            break           
            
    print(final) # 포함되면 1프린트 아니면 0이 프린트된다
