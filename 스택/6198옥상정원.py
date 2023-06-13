import sys
input = sys.stdin.readline

n = int(input())  # 옥상의 수
ans = 0 # 정답 개수 받을 변수
mx= 0 # 최대 높이
stack = [] # 빌딩 높이 저장할 리스트
for i in range(n):  # 빌딩 높이 받을 때마다 계산
    a = int(input()) # 빌딩 높이
    if a >= mx : # 빌딩 높이가 최대 최대 높이 빌딩높이보다 크다면
        mx = a  # 최대값 재설정 
        stack = [a] # 스택에 최대 빌딩만 남겨놓기

    # 스택의 마지막 값을 가장 작은 수로 만들 예정    
    else: # 최대값이 아닐때
        if stack[-1] <= a :  # 현재 빌딩 높이가 스택에 저장된 빌딩 봎이보다 크다면 
            while stack[-1] <= a: #스택에 저장된 빌딩높이중 현재 높이보다 작거나 같은 것들을 모두 뺴내주기
                try: # 그냥 pop시켰더니 EOFError 발생해서 try 문으로 예외처리
                    stack.pop() 
                except EOFError:
                    break
            ans += len(stack) # 스택에 남아있는 빌딩들은 작다고 현재 높이보다 큰 것들만 있으니 정답에 추가
            stack.append(a) # 현재 높이도 스택에 추가
        
        else: #현재 빌딩 높이가 스택마지막 높이보다 작다면
            ans += len(stack) # 스택에 들어간 모든 빌딩 높이보다 작으니 정답에 추가
            stack.append(a) # 현재 빌딩 높이도 스택에 추가
    # print(a, mx)
print(ans) # 정답 출력

