T = int(input()) # 테스트 케이스 개수
for t in range(T):  
    mx = int(input()) # 최대 숫자
    stack = [[] for _ in range(mx)]  # 숫자 개수별 입력받을 list
    for i in range(1, mx+1): # 1부터 최대숫자까지 
        if i == 1: # 1이면 stack[0]에 넣기
            stack[0] = "1"
        else: 
            for j in stack[i-2]: # 2부터 최대 숫자까지는 
                # stack[i-2]의 모든 값들을 받아서
                stack[i-1].append(j+" "+str(i)) # 붙여주거나
                stack[i-1].append(j+"+"+str(i)) # + 후 붙여주거나
                stack[i-1].append(j+"-"+str(i)) # - 후 붙어주기    stack[i-1]자리에

    for i in stack[-1]:  # 스택의 마지막 자리의 것들만 확인 : mx값까지 넣은 값들만 확인
        if eval(i.replace(" ", "")) == 0: # 공백 처리된 값들을 제거 후 eval해서 0이면
            print(i) # 출력
    print()
        
