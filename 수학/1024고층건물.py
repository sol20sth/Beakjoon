n = int(input())
buliding = list(map(int, input().split())) # 고층빌딩 높이
mx = 0  # 최대로 볼 수 있는 개수 받을 변수
li = [[0] * n for _ in range(n)] # 볼 수 있는 빌딩들 저장할 리스트
for i in range(n-1): # 마지막전 빌딩까지 비교
    g =  -1000000001 # 최소 기울기
    for j in range(i + 1, n): # 빌딜 오른쪽만 비교
        if (buliding[j]-buliding[i]) /(j-i) > g: # 기울기가 바로 전의 기울기보다 크다면
            g = (buliding[j]-buliding[i]) /(j-i) # 기울기 재설정
            li[i][j], li[j][i] = 1, 1 # i, j번째 빌딩들은 서로 볼 수 있다고 생각 가능
for i in range(n): # 각각 볼 수 있는 빌딩들의 개수는 리스트에서 한줄씩 빼내서 찾을 수 있음
    mx = max(sum(li[i]), mx) # 각 줄 비교해서 최대값 설정
print(mx)