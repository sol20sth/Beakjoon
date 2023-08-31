n = int(input())  # 용액의 수
li = sorted(list(map(int, input().split())))  # 용액 리스트 정렬

def binary_search(i, end):  # 이진탐색 : 현재위치, 끝 인덱스
    global left, right, mi  
    start = i + 1  # 왼쪽은 i + 1로 고정
    now = li[i]  # 현재 위치 == 오른쪽은 li[i]로 설정
    while start <= end : # 오른쪽 좌표를 결정할 좌측 인덱스가 오른쪽인덱스보다 커지면 종료
        middle = (start + end) // 2 # 중간인덱스 설정
        tmp = now + li[middle]  # 중간값 설정
        if abs(tmp) < mi: # 중간값이 최소값보다 작다면
            mi = abs(tmp) # 최소값 재설정
            left , right = i, middle 
            # 왼쪽, 오른쪽에 i, middle넣기 >> 현재 i, middle번째를 더한게 최소값이라고 찾음
            # 계속 탐색하면서 가장 작은 인덱스 찾기
            if tmp == 0: # 그러나 0이면 더이상 탐색할 필요없기 때문에 함수 끝내기
                return
        if tmp < 0 :  # 중간값이 0보다 작으면 가장 왼쪽이 가장작기때문에 start >> +1
            start = middle + 1
        else:  # 중간값이 0보다 크거나 같으면 가장 오른쪽이 가장크기때문에 end >> -1
            end = middle -1

left, right = 0, 0  # 정답 인덱스 받을 변수
mi = float('inf') # mi 최대로 설정
for i in range(n-1):  # 왼쪽의 좌표를 고정시키고 오른쪽만 이동시키며 찾을예정
    # 그래서 n-2인덱스까지 탐색 : 최대 2개의 값이 필요하기 때문에
    binary_search(i, n-1)

print(li[left], li[right])