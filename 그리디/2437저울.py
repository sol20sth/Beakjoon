n = int(input())
li = list(map(int, input().split())) # 저울추 리스트 
li.sort() # 가벼운 것부터 뽑기 위해서 정렬
sm = 0 # 각각의 합 더할 변수
tf = False # 저울 추 다 더했을때까지 답이 안나올 떄를 대비한 변수
for i in li: # 추 작은 값부터 하나씩 뽑아내기
  if li[0] != 1: # 만약에 1이 없으면 1 출력
    print(1)
    tf = True # 값 찾음
    break
  else: # 1이 있을떄
    if i > sm+1: # 지금까지의 합+1 보다 현재 갑이 크면 
      # 만약 sm+1 <= i 로 비교하면 i 는 i무게를 성립하기 떄문에 sm+1보다 커야지 만들 수 없음 
      print(sm+1) # 지금까지의 합 +1 무게 출력 
      tf = True # 정답찾음 표시
      break
    else: # 해당 되지 않으면
      sm += i # 합에 현재 값을 더해주기
      
if tf == False: # 정답을 찾은적이 없으면
  print(sm+1) # sm은 li의 총합이 담겨있으니 그 값에 + 1을 더해서 만들 수 없는 값이라고 출력

