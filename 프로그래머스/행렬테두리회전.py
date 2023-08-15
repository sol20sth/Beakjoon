def solution(rows, columns, queries):
    answer = []
    li = [[[] for _ in range(columns)] for _ in range(rows)] # 행렬 만들기
    # print(li)
    for i in range(rows):  # row, column에 따라 맞는 숫자 집어넣기
        for j in range(columns):
            li[i][j] = (j+1) + (i*columns)
    for query in queries:   # querys에서 하나씩 빼내서 돌리기
        query = [x-1 for x in query]  # index로 바꿔주기
        y1, x1, y2, x2 = query[0], query[1],query[2], query[3]
        # 시계방향으로 돌리면 한칸씩 먹어가면서 계속 똑같은 수를 이동시키기 때문에 반대로
        tmp = li[y1][x1]  # 돌리는 방향을 반대로 바꿔서 돌리니까 첫번째 숫자가 마지막에 안들어가기 때문에 저장
        mi = tmp  # 최소값을 첫번째 숫자로 일단 저장
        for i in range(y1+1, y2+1):  # 왼쪽 세로 
            li[i-1][x1] = li[i][x1]
            mi = min(mi, li[i][x1])
        for i in range(x1+1, x2+1):   # 아래
            li[y2][i-1] = li[y2][i]
            mi = min(mi, li[y2][i])
        for i in range(y2-1, y1-1, -1):     # 오른쪽 세로
            li[i+1][x2] = li[i][x2]
            mi = min(mi, li[i][x2])
        for i in range(x2-1, x1-1, -1):     # 위ㅉㄱ
            li[y1][i+1] = li[y1][i]
            mi = min(mi, li[y1][i])
        li[y1][x1+1] = tmp  # 다돌리면 마지막 한자리 저장해둔 값으로 넣기
        answer.append(mi) # 최소값 넣기
    return answer
print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))