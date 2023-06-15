word = input() # 주어진 문자열
n = len(word) # 문자열 길이
stack = []  # 문자열 받을 리스트
for i in range(n):  # 처음부터 문자열 길이만큼 반복문
    if word[i] == 'A':  # A이면 스택에 저장
        stack.append(word[i])
    else: # P이면
        if len(stack) < 3: # 스택의 길이가 3미만이면 
            stack.append('P') # 저장시키기
        else: # 3이상이면
            if stack[-3:] == ['P', 'P', 'A']: # 스택의 뒤에 3글자가 PPA이면 
                stack.pop() # P 하나 남기고 지우기
                stack.pop()
            else: # PPAP에 해당이 안되면 P 저장
                stack.append('P')
if stack == ['P']: #모든 작업이 끝났을때 남아있는 알파벳이 P이면 PPAP출력
    print('PPAP')
else:  # P가 아니면 NP 출력
    print('NP')
    