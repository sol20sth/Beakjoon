N = int(input())
line_list = []
count1 = []
for i in range (N):
    line_list.append(list(map(int, input().split())))

def cut(x, y, N):
    for i in range(x, x+N):
        for j in range(y, y+N):
            if line_list[i][j] != line_list[x][y]: # 같아질때까지 구간 반복
                cut(x, y, N//3)
                cut(x, y+N//3, N//3)
                cut(x, y+2*N//3, N//3)
                cut(x+N//3, y, N//3)
                cut(x+N//3, y+N//3, N//3)
                cut(x+N//3, y+2*N//3, N//3)
                cut(x+2*N//3, y, N//3)
                cut(x+2*N//3, y+N//3, N//3)
                cut(x+2*N//3, y+2*N//3, N//3)
                return  
    count1.append(line_list[x][y])
    
cut(0, 0, N)
print(count1.count(-1))
print(count1.count(0))
print(count1.count(1))
    