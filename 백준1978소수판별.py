import sys
input = sys.stdin.readline

T = int(input())

num_list = list(map(int, input().split()))
max_n = max(num_list)  # 받은 수 최댓값
all_n = []

for i in range(1, max_n+1):
    all_n.append(i)  # 최댓값 아래수 리스트

# print(all_n)
nososu = []
for j in range(2, int(max_n**0.5+1)):
    for k in range(2, max_n):
        if j * k > max_n:    # 소수 아닌것들 추출
            break
        else:
            sosu.append(j*k)
list(set(nososu)).append(1)
count = 0
for l in num_list:      # 리스트에서 소수일때마다 카운드 +1
    if l in nososu:
        pass
    else:
        count += 1
print(count)