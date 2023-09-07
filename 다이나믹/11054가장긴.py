n = int(input())

li = list(map(int, input().split()))
#현재위치의 좌우를 비교해서 증가, 감소의 최대 개수 구하기

increase, decrease = [1 for i in range(n)], [1 for i in range(n)]
for i in range(n): # 10자리 모두 탐색  
    for j in range(i): # 다른 한자리 앞에서부터 현재왼쪽자리까지 탐색
        if li[i] > li[j]: # 증가하면
            increase[i] = max(increase[i], increase[j]+1) 
            # 현재 증가하는 개수와, 다른 한자리를 선택:+1 값의 최대값을 업데이트

for i in range(n-1, -1, -1): # 감소는 뒤에서부터 탐색
    for j in range(n-1, i, -1): # 다른점도 오른쪽끝부터 현재의 오른쪽자리까지 탐색하여 
        if li[i] > li[j]: 
            decrease[i] = max(decrease[i], decrease[j]+1)

mx = 0
for i in range(n):
    mx = max(increase[i] + decrease[i] -1, mx) 
# 전체 탐색하여서 감소 증가 더한값들의 최대값찾기 : -1한 이유는 본인을 두번 더한셈이기 때문
print(mx)
