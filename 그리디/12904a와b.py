def f(target):
    while 1: # 크기가 같아질 때까지 반복
        if len(s) == len(target): # target의 길이가 s 와 같아지면 확인
            if s == target: # 같으면
                print(1) # 1 출력
            else:  # 다르면 0 출력
                print(0)
            return 
        # t에서 1개씩 뺴내는 식으로 접근 
        # 마지막이 A이면 마지막 글자만 빼내고 target 재정의
        if target[-1] == 'A': 
            target = target[:-1]
        # 마지막이 B이면 B빼내고 뒤집은 문자열 target으로 재정의
        else:
            target = target[:-1][::-1]
s = input()
t = input()
f(t)

