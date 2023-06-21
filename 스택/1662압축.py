def f1(tmp, li):
    while li: # li가 빌때까지
        a = li.pop() # 뒤에서 부터 하나씩 비교
        if a == ')': # 닫는 괄호이면
            tmp += f1(0, li) # 줄어든 리스트로 탐색
        elif a == '(': # 여는 괄호이면 
            tmp = tmp * int(li.pop()) # tmp(현재까지의 길이) * 여는 괄호 앞으 숫자 곱해주기
            return tmp # 현재의 길이 리턴
        else: # 여는 괄호앞의 숫자가 아닌 숫자이면
            tmp += 1 # 길이 +1
    return tmp # 최종 길이

li = list(input())
ans = f1(0, li)
print(ans)