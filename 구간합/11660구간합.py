# import sys
# input = sys.stdin.readline

# n,m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# for tc in range(m):
#     x1, y1, x2, y2 = map(int , input().split())
#     total = 0
#     for i in range(x1-1, x2): # 행 인덱스
#         total += sum(arr[i][y1-1:y2])
#     print(total)
    
import sys                  
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]   # 주어진 리스트 받기
sum_data = [[0] * (n+1) for _ in range(n+1)]        #리스트의 구간합을 구하기 위한 누적합 리스트

for i in range(1, n+1): 
    for j in range(1, n+1):     # 구간합 리스트의 값은 좌우 누적합에서 작은 사각형인 -1-1인덱스를 가진 인덱스를 한번빼주면 0*0 에서 현재 자리까지의 
                                # 합을 구할 수 있다. 
        sum_data[i][j] = sum_data[i][j-1] + sum_data[i-1][j] - sum_data[i-1][j-1] + arr[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())  
    # 사각형으로 생각해보면 큰 사각형을 터하고 작은 사각형을 더하고 좌우 인덱스를 가지는 사각형을 자르면 
    # x1, y1, x2, y2구간의 합이 구해진다.
    print(sum_data[x2][y2] - sum_data[x1-1][y2] - sum_data[x2][y1-1] + sum_data[x1-1][y1-1])