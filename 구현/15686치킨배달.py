def combi(arr,cnt): # 조합 함수
	ans = [] # 치킨집 좌표 받을 빈 리스트
	if cnt > len(arr): return ans # 필요한 치킨집 개수 받으면 리턴  
	if cnt == 1: # 치킨집개수가 1개필요하면
		for i in arr: 
			ans.append([i]) # 치킨집 좌표 추가 어짜피 1개
	elif cnt>1: # 1보다 크다면
		for i in range(len(arr)-cnt+1): # arr 길이 -cnt 인덱스까지 탐색 >> 인덱스 안벗어나게 조합만들기
			for temp in combi(arr[i+1:],cnt-1): # 하나씩 넣어가며 재귀
				ans.append([arr[i]]+temp)
	return ans

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house , chicken = [], []
for i in range(n):  # 전체 좌표 탐색해서 집이랑 치킨집 좌표 각각의 리스트에 넣기
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
result = (2*n)*n**2+1 # 거리 최대값은 (2*n)*n**2
for x in combi(chicken, m): # 치킨집 m개 뽑아낸 모든 경우의 수
    city_dist = 0 # 치킨거리 값 받을 변수
    for k, l in house: # 집에서 가까운 치킨집거리 찾기
        dist = 2*n+1 # 집에서 치킨집 거리 최소값 받을 변수
        for i, j in x: # 하나의 집에서 치킨집 모두 탐색 
            dist = min(abs(i-k) + abs(j-l), dist) # 최소 거리 찾기
        city_dist += dist # 하나의 집마다 최소의 거리 찾은 후 + 해주기
    result = min(result, city_dist) # 결과값에 치킨거리 최소값 계속 찾기
print(result)
