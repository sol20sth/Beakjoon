n = int(input())
li = list(map(int, input().split())) # 수열의 각 원소 받은 리스트
mx = 0  # 최대값 변수
stack = []  # 오른쪽에 있는 수들을 저장할 스택
for i in range(len(li)-1, -1 ,-1): # 리스트에서 뒤에서부터 탐색예정
    if mx <= li[i]:  # 만약 최대값보다 크거나 같다면
        mx = li[i] # 최대값 재설정
        li[i] = -1 # 자기보다 오른쪽에는 큰 수가 없다고 생각하고 -1로 변경
        stack = [mx] # 현재 자기 오른쪽은 다 자신보다 작으니 스택도 자기 자신만 들어가 있도록 재설정
    else: # 최대값보다 작다면
        for _ in range(len(stack)): # 스택의 길이만큼 반복
            if stack[-1] > li[i]: # 만약 스택의 마지막 수보다 작다면 
                tmp = li[i] # 현재 자신의 숫자를 하나의 변수로 저장 후 
                li[i] = stack[-1] # 현재 자신을 스택의 마지막 수로 재설정
                stack.append(tmp) # 스택에 원래 자기 자신을 넣고
                break #반복문 종료 >> 왼쪽 수로 넘어가기
            else:  # 만약 스택의 마지막 수보다 크다면 
                stack.pop() # 스택에는 필요가 없다고 생각하고 스택의 마지막 수를 없애기
    # print(stack)
print(*li) # 출력