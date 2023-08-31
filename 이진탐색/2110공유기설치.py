n, c = map(int, input().split()) # 집 개수, 공유기 개수
xn = sorted(list(int(input()) for _ in range(n)))  # 이진탐색 하기위해 정렬해서 받기
ans = 0 # 정답받을 변수
def binary_search(start, end): # 설치거리, 최대거리
    global ans
    while start <=  end: # 설치거리이 최대설치거리보다 커지면 종료
        middle = (start + end)//2  # 중간값 설정
        now = xn[0]  # 현재위치 맨앞위치로 설정
        cnt = 1  # 맨앞에 공유기 설치하는 것으로 설정
        # print(start, middle, end , now, cnt)
        for i in range(1, len(xn)):   # xn리스트를 첫번째 현재 위치 제외하고 탐색
            if xn[i] >= now + middle: # xn[i]가 중간위치보다 크거나 같으면
                cnt += 1  # 공유기 설치
                now = xn[i]  # 현재위치 xn[i]로 설정
        if cnt >= c:  # 모든 공유기 설치 후 공유기 개수가 설치해야하는 공유기 개수를 만족 == 크거나 같으면
            start = middle + 1 # 설치거리를 중간값 + 1 로 재탐색
            ans = middle  # 일단 만족하니 정답으로 처리 : 더큰 설치거리가 나오면 다시 처리됨
        else:  # 개수가 만족하지 못하면 거리가 더 짧아져야함 : 최대거리를 1 줄이고 재탐색
            end = middle - 1

        
binary_search(1, xn[-1]-xn[0])  # 처음거리는 1, 최대거리는 집사이의 최대거리로 설정 후 함수 실행
print(ans)