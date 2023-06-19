T = int(input()) # 테스트 케이스 개수
for tc in range(T):
    w = input() # 문자열
    k = int(input()) # 문자열길이
    w_dict = {} # 알파벳 딕셔너리
    mx, mi, tf = 0, 10001, 0 # 최대, 최소, 연속문자열있는지 판단 변수
    for i, j in enumerate(w): # 문자열에서 각 문자열의 인덱스 찾아내기
        # print(i, j)
        if j in w_dict: # 딕셔너리 안에 해당 문자열이 있으면
            w_dict[j].append(i) # 해당 문자열에 인덱스 추가
        else: # 없으면
            w_dict[j] = [i] # 해당 문자열 인덱스만 추가된 리스트로 만들기
    for i in w_dict: # 문자열 하나하나의 인덱스 리스트를 뽑아내서 반복문 돌릴예정
        check_index = w_dict[i] # 문자열 하나하나의 인덱스 리스트
        n = len(check_index) # 문자열에서 해당 문자가 몇개 있는지 확인하는 변수
        if n < k : # 개수가 성립하지 않으면 넘어가기
            continue 
        else: # 개수가 성립하면 
            tf = 1 # 문자열있다고 체크
            for j in range(n-k+1): # 들어간 알파벳 숫자를 k개로 맞추기 위해서 n-k 까지 앞에서 부터 리스트 슬라이스
                mx = max(mx, check_index[j+k-1] -check_index[j] + 1) # 최대 최소값 재설정
                mi = min(mi, check_index[j+k-1] -check_index[j] + 1)
    if tf == 1: # 해당 문자열이 있으면 최소 최대 출력
        print(mi, mx)
    else:  # 없으면 -1 출력
        print(-1)