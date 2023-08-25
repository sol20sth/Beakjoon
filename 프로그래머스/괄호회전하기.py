def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        answer += f(s, i, n)  # 괄호가 성립하는지 1칸씩 오른쪽으로 이동시키며 확인하기
    return answer

def f (s, i, n):  # 괄호가 유효한지 아닌지 확인 함수
    stack = []  # 괄호 넣을 스택
    for j in range(n):  # 시작점부터 n개까지 모두 탐색
        if s[(j+i)%n] == '{' or s[(j+i)%n] == '(' or s[(j+i)%n] == '[' : # (j+i)%n 이 열리는 괄호면 스택에 넣기
            stack.append(s[(j+i)%n])
        elif s[(j+i)%n] =='}':         #(j+i)%n이 닫히는 괄호였을때 스택의 [-1]번째가 같은 열리는 괄호이면 스택에서 빼기
            if stack and stack[-1] == '{':
                stack.pop()
            else:   # 아니라면 유효하지 않다고 생각해서 0리턴 >> 끝내기
                return 0
        elif s[(j+i)%n] ==']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return 0
        elif s[(j+i)%n] ==')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0
    if not stack:  # 스택이 비어있다면 return 1 >> 유효
      return 1
    return 0 #비어있지 않다면 : 모두 열린괄호 : 0리턴 >> 유효x
