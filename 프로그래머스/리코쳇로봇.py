def solution(board):
    answer = 0
    y, x = len(board), len(board[0]) 
    robot = [0, 0]
    for i in range(y):
        for j in range(x):
            if board[i][j] == "R":
                robot = [i, j]
            elif board[i][j

                
    return answer

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]	))