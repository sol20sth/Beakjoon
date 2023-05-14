def gcd(a, b):  # 최대 공약 수 찾는 함수
    if a < b:  # a가 b보다 작으면 위치 변경
        a, b = b, a
    while b != 0: # 나누어 떨어질떄까지 반복
        a %= b  # 나누고 위치 변경
        a, b = b, a 
    return a # 최대 공약수 리턴

import sys
input = sys.stdin.readline

n = int(input())
li = sorted(list(int(input()) for _ in range(n)))  # 정렬해서 숫자 받기
res_gcd = li[1] - li[0] # 숫자들의 차이의 최대 공약 수 
for i in range(1, n-1):
    res_gcd = gcd(res_gcd, li[i+1] - li[i])  
    # 최대 공약수 찾기 2개씩비교해서 차이들의 최대공약수 재설정 
div = set()
for i in range(1, int(res_gcd**0.5) + 1): # 최대공약수의 제곱근까지
    # 나누어 떨어지는지 확인 후 나누어 떨어지면 공약 수라고 생각하고 
    # set에 추가 a*b = res_gcd 라면 둘모두 공약수 >> 모두 추가
    if res_gcd % i == 0:
        div.add(i)
        div.add(res_gcd // i)
div.remove(1) # 1은 제외
print(" ".join(map(str, sorted(div)))) # 정렬 후 출력