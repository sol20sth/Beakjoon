n = int(input())

prime = [True for _ in range(n+1)] 
#에라토스테네스의 체 알고리즘
for i in range(2, int(n ** 0.5)+1):
    if prime[i]:
        for j in range(i+i, n+1, i):
            prime[j] = False 
primeLi = [i for i, j in enumerate(prime) if j == True and i >=2 ]

# 누적합 구하기
primeSum = [0] # 누적합 변수 , 본인이 소수일떄도 생각해야하니까 0도 넣기
for i in range(len(primeLi)): # 길이만큼 primeLi 전체 누적합 구하기
    if primeLi[i] > n: # 누적합이 구할 수보다 크다면 멈추기
        break
    primeSum.append(primeSum[-1] + primeLi[i]) # 누적합 append
# print(primeSum)
cnt = 0 # 결과값 개수 저장 변수
ln = len(primeSum) # 누적합 리스트 길이 변수

for i in range(ln-1, -1, -1): # 뒤에서부터 뺴면서 접근
    if primeSum[i] < n: # primeSum[i]-primeSum[j]으로 탐색할건데 primeSum[i]가 n보다 작다면 성립 x
        break
    for j in range(i-1, -1, -1): # 뺄 수는 i보다 앞에있는 수부터
        if primeSum[i]-primeSum[j]== n: # 뺏을떄 n이라면 
            # print(i, j)
            cnt += 1 # 결과값 +1 해주기
        elif primeSum[i]-primeSum[j] > n: # 뺏을때 n보다 커진다면 다음수로 넘어가기
            break
print(cnt)

# prime = [True for _ in range(4000001)]

# for i in range(2, int(4000001 ** 0.5)):
#     if prime[i]:
#         for j in range(i+i, 4000001, i):
#             prime[j] = False 
# primeLi = [i for i, j in enumerate(prime) if j == True and i >=2 ]

# n = int(input())

# primeSum = [0]
# for i in range(len(primeLi)):
#     if primeLi[i] > n:
#         break
#     primeSum.append(primeSum[-1] + primeLi[i]) 

# cnt = 0
# ln = len(primeSum)

# for i in range(ln-1, -1, -1):
#     if primeSum[i] < n:
#         break
#     for j in range(i-1, -1, -1):
#         if primeSum[i]-primeSum[j]== n:
#             # print(i, j)
#             cnt += 1
#         elif primeSum[i]-primeSum[j] > n:
#             break
# print(cnt)