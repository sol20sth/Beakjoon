import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
lenarr = len(arr)       # arr 길이
sumarr = [0] * (lenarr+1)   # 구간합구하기 위해 0 하나 추가
maxx = -1000000
for i in range(1, lenarr+1):
    sumarr[i] = arr[i-1] + sumarr[i-1]  # 앞의 수를 모두 더한값을 넣은 새로운 리스트
# print(sumarr)
for j in range(lenarr-k+1):     
    if (sumarr[j+k] - sumarr[j]) > maxx:       # k 길이의 구간합이 maxx 보다 크면 넣어주기
        maxx = (sumarr[j+k] - sumarr[j])
        
print(maxx)