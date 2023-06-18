n = int(input())
li = list(map(int, input().split())) # 리스트 숫자들

dp = n * [1] # x번쨰의 가장 긴 수열의 길이 저장 dp

for i in range(n): # 배열길이만큼 반복
    for j in range(i): # 해당 리스트의 앞 원소까지 비교
        if li[i] > li[j]: # 현재의 값이 앞의 숫자 들보다 작을 때마다 비교
            dp[i] = max(dp[i], dp[j] + 1) # 최대값을 갱신해주기 : 현재의 dp, 앞의 dp[j]+1과 비교
            # dp[j] + 1인 이유는 j번째보다 i가 크기 때문에 i 번째까지 넣은 값이 최대 리스트 길이니까
mxlen = max(dp) # 최대 길이 찾기
print(mxlen) # 출력
stack = [] # 최대 리스트 원소 찾을 스택
for i in range(n-1, -1, -1): # 뒤에서부터 비교
    if dp[i] == mxlen: # 최대 값이라면 
        stack.append(li[i]) # 스택에 해당 원소를 넣고 
        mxlen -= 1 # 최대 길이 숫자 하나 뺴기
stack.sort(key=lambda x : x) # 오름차순 정렬 >> 최대 값부터 넣었기 떄문에
print(*stack) 