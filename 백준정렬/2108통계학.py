# 산술평균 , 중앙값, 최빈값, 범위
# 더해서 전체 개수로 나누기
# 2n - 1 // 2
# count
# max min
import sys
input = sys.stdin.readline
T = int(input())
list_num = [int(input()) for i in range(T)]
index_num = len(list_num)
# print(list_num)
# 산술평균
print(sum(list_num) // index_num)
# 중앙값 
list_num.sort()
print(list_num[(index_num -1)//2])
# 최빈값
countt = [] # 최빈수 리스트
maxxx = 0
all_num = set(list_num) # 리스트에 포함된 숫자들만 뽑아서 확인해보기
for i in all_num:
    if maxxx == list_num.count(i): # 최빈수랑 숫자랑 같으면 숫자추가
        countt.append(i)
    elif maxxx < list_num.count(i):# 최빈수보다 숫자개수가 높으면 최대값리스트 초기화
        countt = []
        maxxx = list_num.count(i)
        countt.append(i) # 최빈수 다시추가
countt.sort()  # 최빈수 리스트 정렬 >> 2번째 수 뽑기위해
# print(countt)
if len(countt) == 1:    # 최빈수가 1개일때 
    print(countt[0])
else:       # 최빈수가 여러개일때 2번째 수 뽑기
    print(countt[1])
    
# 범위
print(max(list_num) - min(list_num))
#####count를 사용할 시 시간복잡도가 상승해서 시간초과떠서 아래코드처럼 작성해야함




#### 시간초과 안당하려면 아래방법으로 풀기

import sys
from collections import Counter
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))
 
# 산술평균 - 다 더해서 / n
print(round(sum(li)/n))
 
# 중앙값 - 오름차순 -> 중간값
li.sort()
print(li[n//2])
 
# 최빈값 - 빈출
cnt_li = Counter(li).most_common()
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]: #최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])
 
# 범위 - 최댓값-최솟값
print(max(li)-min(li))
    
    


