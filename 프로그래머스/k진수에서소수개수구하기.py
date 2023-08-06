def prime(num):  # 소수 구하는 함수
    if num ==1 :
        return 0
    elif num ==2:
        return 1
    elif num == 3:
       return 1
    else:
      for i in range(2, int(num**0.5)+1):
        if num % i == 0:
          return 0
      else:
        return 1

def solution(n, k):
    answer = 0
    a = ''			# a에 k진수 수 저장 할 예정
    while n:   # n이 0이 아닐때까지 반복
        a +=str(n % k)  # n%k 를 계속 a에 넣기
        n = n // k  # n계속 업데이트 
    a = a[::-1]  # 완료된 a를 거꾸로 돌려야 k진수로 바뀜
    li = list(map(str, a.split("0"))) # "0"을 기준으로 모두 자르기
    while "" in li:        # li에 ""이 있으면 모두 없애주기
       li.remove("")
    for i in li:        # li에 있는 값들 모두 prime확인 후 소수이면 
       if prime(int(i)) ==1:
          answer += 1    # answer에 +1해주기
    return answer