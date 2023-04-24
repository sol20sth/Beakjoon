T = list(map(str, input().split('-')))  # '-' 있는 곳을 나누어준다
m = []              #ex) 2+3-4-5 >> -나올때까지 더해주고 그뒤로 다빼주는 식으로 만들 예정
n = []
total = 0
for i in range(len(T)):     # '+'들어가있을때 초기값을 더해주어서 total에 넣는다.
    if i == 0:
        if '+' in T[i]:
            n = list(map(int, T[i].split('+')))
            total = sum(n)
        else:
            total = int(T[0])    # '+'없을때는 그냥 입력값을 초기값으로 설정
    else:        
        if '+' in T[i]:
            m = list(map(int, T[i].split('+')))    # '+'있을때 더해준다음에 리스트의 합을 total 에서 빼준다
            total -= sum(m)
        else:
            total -= int(T[i])  # '+'없을떄 그냥 빼준다
print(total)
