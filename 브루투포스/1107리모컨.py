num = int(input()) # 목표 숫자
n = int(input()) # 고장난 숫자 개수
if n != 0: # 고장난 숫자가 있으면
    broken = list(map(int, input().split())) # 고장난 숫자 리스트
    mi = abs(100-num) # 최소 누른 숫자 +- 로만 움직인 수로 설정
    if len(broken) == 10: # 고장안난 숫자가 없을 경우
        print(mi) # +, - 로만 움직인 수 출력
    else: 
        for i in range(0, 1000001): # 최대수 500000이기때문에 모두다 고장났다고 생각하면
            # 1000000에서 -한 값을 찾는 경우의 수를 생각해 1000000까지 찾기
            for j in str(i): # 숫자 i에 들어있는 수가 broken에 들어있으면 멈추기
                if int(j) in broken:
                    break
            else: # 고장난 수가 없으면 최소값 비교
                mi = min(mi, abs(i-num)+len(str(i))) # 해당 숫자에서 목표숫자 뺴고 해당 숫자의 길이만큼 더해서 비교
        print(mi)
else: # 고장난 숫자가 없으면
    print(min(len(str(num)), abs(num-100))) # 목표 숫자-100 or 목표숫자 길이
        

