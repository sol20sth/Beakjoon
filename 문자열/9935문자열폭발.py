
st = input()    # 받은 문자열
target = input() # 찾아야 할 문자열
n, m = len(st), len(target)  # 각각의 문자열의 길이 설정
stack = [] # 타겟에 해당하는 문자열만 저장할 리스트
stack2 = [] # 정답을 저장한 리스트
for i in range(n): # st전체 탐색
    if st[i] in target: # 해당 문자열이 target에 들어가는 문자열이라면
        if len(stack) >= m-1 and st[i] == target[-1] : 
            # 타겟에 저장된 문자열이 타겟문자열 길이보다 크거나 같고, 
            # 해당 문자가 찾아야할 문자열의 마지막과 같으면
            for j in range(m-1): # 타겟의 길이만큼 뒤에서부터 같은지 비교
                if stack[-1-j] != target[-2-j]: 
                    # 만약 같지 않다면 해당 문자열로는 타겟을 만들 수 있는 경우의 수는 없다.
                    stack2.extend(stack) # stack들어간 문자열들로는 타겟을 만들수 없으므로 
                    # 따라서 정답문자열 리스트에 추가해주고 빈리스트로 다시 만들기 
                    stack = [] 
                    stack2.append(st[i]) # 그리고 해당 문자열도 target을 만들 수 없기 떄문에 추가
                    break #반복문 종료 >> 다음 문자열로 이동
            else: # 뒤에서부터 비교했을때 스택에 저장된 값이 target이라면
                for _ in range(m-1): # 스택에는 타겟의 마지막 문자열을 제외하고
                    # m-1개만큼 들어가 있기 때문에 m-1번 제거해준다
                    stack.pop()
        
        else: # 해당 문자가 타겟을 비교 할 만한 조건이 되지 않으면 
            stack.append(st[i]) # 스택에 추가
    
    else:  # 해당 문자가 target과는 상관 없는 문자이면
        stack2.extend(stack) # 스택에 있는 값들은 target이 불가능하다고 생각하고
        # 스택을 정답리스트에 추가 후 스택을 빈리스트로 만들기
        stack = []
        stack2.append(st[i]) # 해당 문자 또한 정답리스트에 추가
stack2.extend(stack) #모든 문자열을 탐색 완료했을떄 스택에 남아있는 문자들도 target을 
# 만들 수 없으므로 정답리스트에 추가
if stack2: # 정답리스트가 남아있다면 출력
    print("".join(map(str, stack2)))
else: # 남아있지 않으면 FRULA 출력
    print('FRULA')