def div(li, b):
    ans = [[0] * n for _ in range(n)] # 정답 받을 리스트
    if b == 1: # 반복횟수1일때 
        for i in range(n): # 행렬의 원도들이 1000이상일 수도 있으니 나머지값으로 바꿔서 리턴
            for j in range(n):
                li[i][j] %= 1000
        return li
    elif b % 2 == 1: # 홀수 일때
        li2 = div(li, b-1) # A**(b-1)  *  A 로 설정하기 위해 li2만들기
        for i in range(n):  # 곱셈처리 한 후 1000으로 나누어 리턴
            for j in range(n):
                for k in range(n):
                    ans[i][j] += li2[i][k] * li[k][j]
                ans[i][j] %= 1000
        return ans
    else: # 짝수 일때
        li2 = div(li, b//2)  # A**(b//2)  * A**(b//2)로 설정하기 위해 li2만들기
        for i in range(n):  # 곱셈처리 후 1000으로 나누어 리턴
            for j in range(n):
                for k in range(n):
                    ans[i][j] += li2[i][k] * li2[k][j]
                ans[i][j] %= 1000
        return ans

n, b = map(int, input().split()) # 행렬크기, 반복 제곱횟수
li = [list(map(int, input().split())) for _ in range(n)] # 행렬

ans = div(li, b) # 정답 출력처리
for i in range(n):
    print(*ans[i])