import sys
input = sys.stdin.readline  # 한줄 씩 입력 받음 >>> 시간 줄어듬
def push(x):
    all.append(x)       # 맨 끝에 추가
def top():              # 빈리스트면 -1 
    if all == []:
        print(-1)
    else:               # 아니면 끝 프린트
        print(all[-1])
def pop():              # 비어있으면 -1 아니면 마지막 프린트후 제거
    if all == []:
        print(-1)
    else:
        print(all[-1])
        all.pop()
    
def empty():            # 비어있는지 확인
    if all == []:
        print(1)
    else:
        print(0)
def size():             # 리스트 크기
    print(len(all)) 
T = int(input())
all = []
for i in range(T):
    comm = input().split()      # ' '가 있으면 스플릿하고 없으면 하나로 잡아서 리스트의 인덱스로 접근가능
    order = comm[0]     

    if order == 'push':     # 조건 만족할 때 함수 발동
        push(comm[1])
    elif order == 'pop':
        pop()
    elif order == 'size':
        size()
    elif order == 'empty':
        empty()
    elif order == 'top':
        top()