T = int(input())
for i in range(T):
    
    numbers = []
    
    for j in range(9):
        numbers.append(list(map(int, input().split())))

    count = 0
    for k in range(9):
        down_list = []
        if len(set(numbers[k])) != 9:
            count += 1
            
        for l in range(9):
            down_list.append(numbers[l][k])
        if len(set(down_list)) !=9:
            count += 1

            
    dot = []
    
    def squar_dot(count, numbers,dot):
        for z in range(3):
            for x in range(3):
                for m in range(3):
                    for n in range(3):
                        dot.append(numbers[m+x*3][n+z*3])
                    if len(set(dot)) != 9:
                        count += 1
        return count

    squar_dot(count, numbers,dot)

    if count == 0:
        print(f"#{i+1} 1")
    else:
        print(f"#{i+1} 0")
