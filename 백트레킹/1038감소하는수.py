n = int(input())
cnt = -1 # 0이 0번째이니까 
stack = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# 감소하는 수로 0~9까지 넣어놓고 시작하였다
++++ㄴ
def check_down(i): # 감소하는 수인지 체크하는 함수
  for j in range(len(i)-1): # 감소하지 않으면 0, 감소하는 수이면 1리턴
    if i[j] <= i[j+1]:
      return 0
  return 1

tf = False  # 감소하는 수가 출력되었는지 확인하는 변수
for i in stack:  #스택에서 하나씩 빼서 확인
  cnt += 1  # 스택에 들어가있는 것은 모두 감소하는 수이므로 cnt += 1
  if cnt == n: # n번째 감소하는 수이면 
    tf = True # 감소하는 수라고 체크 후 출력 후 반복문 종료
    print(i)
    break
  for j in range(10):  # 현재 감소하는 수에서 뒤에 0~9까지 터한 값으로 감소하는 수 확인
    tmpStr = i + str(j)
    tmpCheck = check_down(tmpStr)
    if tmpCheck: # 감소하는 수라면 스택에 넣기
      stack.append(tmpStr)
if tf == False: # 감소하는 수가 없다면 -1 출력
  print(-1)