
def solution(board):
    def bfs(start):
      dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
      n = len(board)
      opened = [start]
      closed = [[987654321 for _ in range(n)] for _ in range(n)]
      answer = -1
      while opened:
          y, x, d, c = opened.pop(0)

          for dd in range(4):
              yy, xx = y+dy[dd], x+dx[dd]  
              if 0<=yy<n and 0<=xx<n and board[yy][xx] ==0:
                cost = c + (100 if d == dd else 600)
                if closed[yy][xx] > cost:

                  closed[yy][xx] = cost
                  opened.append([yy,xx, dd, cost])
      return closed[-1][-1]
    return min(bfs([0, 0, 1, 0]), bfs([0, 0, 3, 0]))