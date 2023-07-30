n = int(input()) # 최대 숫자
stack = [] # 저장할 리스트
tmp = 1  # 몇번째 숫자까지 저장한지 기억할 변수
res = [] # +, - 순서 저장
tf = True # no인지 아닌지 판단
for i in range(n): 
    x = int(input())
    while tmp <= x:  # 해당숫자가 현재 저장한 숫자보다 작다면 
        stack.append(tmp)  # push해주고 
        res.append("+")  # res에 +넣어주기
        tmp += 1  # 숫자 넣어줬으니 사용처리
    if stack[-1] == x:  # stack의 마지막 숫자가 input이랑 같으면 pop
        stack.pop()
        res.append("-")
    else:  # 다르면 불가능하니 No
        tf = False  # tf 불가능 처리
        print("NO")
        break
if tf == True:  # 모든 작업이 끝났을때 tf가 True이면 
    for i in res:  # res에 들어간 +, -를 차례로 출력
        print(i)