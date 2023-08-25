def solution(n, left, right):
    answer = []
    left_row , left_col = left//n, left%n     # left의 row, col 위치 찾기
    right_row , right_col = right//n, right%n # right의 row, col 위치 찾기
    for i in range(left_row, right_row+1):  # 사이의 row만 탐색 
        for j in range(n):  # col 탐색
            if  i == left_row and j < left_col: # left보다 왼쪽에 있으면 continue
                continue
            elif i == right_row and j > right_col: # right보다 오른쪽에 있으면 끝내기
                break
            else: # 나머지는 사이에 있다고 생각하고 넣기
                answer.append(max(i, j)+1)

    return answer

print(solution(3,2,5))