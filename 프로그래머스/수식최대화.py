from itertools import permutations
def solution(expression):
    answer = 0
    li1, li2 = [], [] # 숫자, 기호를 저장할 빈리스트
    tmp = ''  # 숫자들을 하나씩 탐색할때 여러자리일때 저장할 변수
    for i in range(len(expression)):  # 전체 문자열 탐색
        if i == len(expression)-1:      # 마지막 자리이면 tmp를 숫자로 저장
            li1.append(tmp+expression[i]) 
        elif expression[i] == "+" or expression[i] =='-' or expression[i] == '*':
        # 기호이면 tmp에 저장된 숫자 저장 , 기호 저장, tmp초기화
            li1.append(tmp)
            li2.append(expression[i])
            tmp = ''
        else:     # 숫자이면 tmp에 숫자 저장
            tmp += expression[i]
    a = permutations(['+', '-', '*'], 3)  # +, -, *로 가능한 순열 모두 찾아서 tmp에 저장
    tmp = []
    for i in a:
        tmp.append(i)

    for i in tmp:     # 순열 하나하나 탐색하기
        tmp1, tmp2 = li1[::], li2[::]   # 숫자, 기호들 복제해서 확인
        for j in i:     # 순열의 i 의 문자열j가 tmp2에 들어있을때까지 반복
            while j in tmp2:
                idx1 = tmp2.index(j) # 해당 j의 tmp2인덱스를 찾아서
                tmp1.insert(idx1, str(eval(tmp1.pop(idx1)+tmp2.pop(idx1)+tmp1.pop(idx1))))
                # tmp1에서 해당인덱스의 숫자를 꺼내고 tmp2문자열 빼내고 첫번째 숫자를 꺼냈으니 길이가 1
                # 줄어서 다시 해당인덱스의 숫자를 꺼내서 더해주기
        answer = max(abs(int(tmp1[0])), answer)  # 모든 반복문 끝나면 tmp1에 숫자가 한개 존재
        # 남은 값이 최대값인지 확인 후 answer에 저장
    return answer
