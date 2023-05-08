def f(a, b):
    global c  
    if b == 1: # 나눌 횟 수 1이면 
        return a % c # 마지막으로 나눈 나머지 리턴
    elif b % 2 == 0: # 나눌횟수 짝수이면
        return (f(a,b//2)**2)%c # 절반 분할 후 함수재귀 >> 제곱 후 나머지 
    else: # 홀수이면 횟수 1개 비니까 a한번더 곱한후 나머지
        return ((f(a,b//2)**2)*a)%c
a, b, c = map(int, input().split())
print(f(a, b))