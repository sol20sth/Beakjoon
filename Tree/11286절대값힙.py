import sys
input = sys.stdin.readline

def enq(x):
  global last   # 숫자 넣을 인덱스
  last += 1     # 1부터 시작
  tree[last] = x  # 입력받은 숫자를 넣을 곳에 넣기
  # print(tree)
  c = last    # 자식 c
  p = c//2    # 부모 == 자식 //2 인덱스
  while p and abs(tree[p]) >= abs(tree[c]):   # 부모인덱스가 0이아니고 부모의 절대값이 클떄만 돌린다 >>> 부모가 작아질때까지 반복
    if abs(tree[p]) == abs(tree[c]):    # 만약 절대값이 같다면
      tree[p], tree[c] = min(tree[c], tree[p]), max(tree[c], tree[p])   # 큰값을 자식 작은값을 부모에 넣는다
    else:
      tree[c], tree[p] = tree[p], tree[c]   # 절대값이 자식이 작다면 바꿔주기
    c = p       # 부모 , 자식 인덱스 새로 할당
    p = c//2
  
def deq(x):
  # print(tree)
  global last
  tmp = tree[1]   # 최소값을 일단 빼내고 저장
  tree[1] = tree[last]    # 마지막 인덱스에 저장된 값을 1번자리로 옮김
  tree[last] = 0      # 옮겼으니 마지막 인덱스 0으로 바꾸기
  last -= 1   # 라스트 인덱스 -1해주기
  p = 1     # 부모 1, 자식 p*2
  c = p*2
  while c <= last:    # 자식인덱스가 마지막 입력 인덱스보다 작을떄만
    if c+1 <= last and abs(tree[c]) > abs(tree[c+1]):     # 오른쪽 트리가 있고 오른쪽 값이 더 작으면 오른쪽이랑 비교
            c += 1      
    elif c+1 <= last and abs(tree[c]) == abs(tree[c+1]):  # 오른쪽 트리가 있고 절대값이 같으면 
            if tree[c] > tree[c+1]:                       # 오른쪽이 작으면 오른쪽이랑 비교 
              c += 1                                      # 왼쪽이 더 작으면 왼쪽이랑 비교 >> 값바꿀필요 x
            
    if abs(tree[c]) < abs(tree[p]) :            # 절대값이 부모다 더클때
      tree[c], tree[p] = tree[p], tree[c]       # 자식 부모 변경
      p = c                                     # 새로운 값 할당
      c = p * 2
    elif abs(tree[c]) == abs(tree[p]):        # 같으면
      tree[p], tree[c] = min(tree[c], tree[p]), max(tree[c], tree[p]) # 작은값 부모 큰값 자식
      p = c
      c = p * 2
    else:
      break
  print(tmp)    # 처음에 뽑았던 최소값 프린트
  
n = int(input())
last = 0
tree = [0] * (n+1)    # 트리 구현하기 위한 빈 리스트
for _ in range(n):
  num = int(input())    # 숫자받기
  if num != 0:      # 숫자가 0이 아니면 enq(num)
    enq(num)
  else:             # 숫자가 0이면
    if tree[1]==0:    # 트리top가 0이면 0출력
      print(0)
    else:             # 트리top이 0이아니면 deq
      deq(num)


  
  
  