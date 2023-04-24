import sys
input = sys.stdin.readline

T = int(input())    # 숫자 개수
nums = list(map(int, input().split()))  # 한줄 받은거 리스트로 정리
nums.sort()     # 리스트 올림차순 정렬 >> 최소값구하기 위해
# print(nums)
sum = 0
for i in range(T):
    sum += nums[i] * (T-i)  # 제일 작은수부터 T-i 곱해주면서 더하기
    # print(sum)
print(sum)