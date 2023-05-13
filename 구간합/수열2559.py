# import sys
# input = sys.stdin.readline
# a, b = map(int, input().split())
# arr = list(map(int, input().split()))
# mx = 0
# for i in range(a-b):
#     sum = 0
#     for j in range(b):
#         sum += arr[i+j]
#     if sum > mx:
#         mx = sum        
# print(mx)



import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
lenarr = len(arr)
sm = [0] * (lenarr+1)
mx = -1000000
for i in range(1,lenarr+1):
    sm[i] = arr[i-1] + sm[i-1]
print(sm)
for j in range(lenarr-k+1):
    if (sm[j+k] - sm[j]) > mx:
        mx = (sm[j+k] - sm[j])
        
print(mx)