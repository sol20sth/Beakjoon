n, m = map(int, input().split())
li = list(map(int, input().split()))

ans = 0 # 정답변수
mx_left, mx_right = 0, 0 # 왼쪽 오른쪽 최대 높이
for i in range(1, len(li)-1):  # 첫번째 마지막 제외하고 찾기 : 각각의 left, right의 최소값이 0이기 떄문에
    mx_left = max(li[:i]) # 왼쪽의 가장 높은 높이 
    mx_right = max(li[i+1:])  # 오른쪽의 가장 높은 높이
    
    tmp = min(mx_left, mx_right)  # 왼쪽, 오른쪽에서 작은 값
    
    if li[i] < tmp:  # 양쪽으 높이의 작은값보다 작다면 빗물이 고임
        ans += tmp - li[i] # 정답에 차만큼 더해주기

print(ans)