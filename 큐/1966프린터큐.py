import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    n , m = map(int, input().split())   # n: 받을숫자길이, m : 목표인덱스
    arr = list(map(int, input().split()))   # 받는숫자 리스트
    front = 0       # 확인할 인덱스
    mx = max(arr)   # 배열 최대값
    stack = []      # 빈 스텍
    while True:     
        if arr[front] == mx:    # 뽑은 배열이 최대값일때
            if front == m:      # 뽑은 배열이 목표인덱스일때 끝
                break
            else:       # 목표인덱스가 아닐때
                stack.append(arr[front])    # 스택에 추가
                arr[front] = -1         # 값 -1로변경
                front = (front+1) % n       # 뽑을 위치 한칸오른쪽
                mx = max(arr)       # 최대값 재설정
        else:       # 최대값 아닐때 
            front = (front+1) % n # 뽑을위치 한칸 오른쪽
            continue

    print(len(stack)+1)
