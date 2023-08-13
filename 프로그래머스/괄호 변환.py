def checkvaild(u): # u가 유효한지 아닌지 판별
    q = []
    for i in u: # u의 문자들을 다 확인
        if i == "(":
            q.append(i) # ( 이면 q에 추가 
        else:  # ) 이고 
            if len(q) == 0: # q가 비어있으면 False return
                return False
            elif q[-1] == ')':  # ) 이어도 False
                return False
            else:     # (일때 한쌍이라 생각하고 q에서 (빼내기
                q.pop()
    return True       # 모든 u의 문자열이 쌍으로 만족하면 True return

def process(p): # p를 나누는 과정
    if not p:     # 빈 문자열이면 빈문자열 리턴
        return p
    tmp1, tmp2 = 0, 0
    for i in range(len(p)):  # (, )의 개수가 같아질때까지 확인
        if p[i] == '(':
            tmp1 += 1
        else: tmp2 += 1
        if tmp1 == tmp2:   # 개수가 같아지면 그곳을 기점으로 u, v로 나누기
            break
        
    u, v = p[:i+1], p[i+1:]  # u, v를 i번째로 나누기

    if checkvaild(u) == True:  # u가 올바른 괄호 문자열이면
        return u + process(v) # u에 process(v) 한값을 더해준 값을 리턴 == v를 새로운 p로 생각
    else:   # 올바르지 않다면
        stack = '(' + process(v) +')'  # 빈문자열에 ( +  process(v) + ) 값을 더해주고 저장
        for i in range(1, len(u) -1):  # u를 확인할예정 >> 0번 , -1 인덱스를 제외하고 값을 뒤집어주고 더해주기
            if u[i] == '(':
                stack += ')'
            else:
                stack += '('
    return stack    # 모든 과정이 끝나면 stack을 빼내기

def solution(p):
    answer = ''
    answer = process(p)   # 빼낸 stack값 출력
    return answer

print(solution("()))((()"))

