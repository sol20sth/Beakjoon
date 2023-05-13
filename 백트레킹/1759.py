def back(start): 
    if len(s) == l: # 문자열 받은 리스트의 길이가 목표 리스트의 길이라면
        cnt = 0  # 모음 갯수 샐 변수
        for i in s: # 하나씩 빼서 비교
            if i in gather: # 모음이라면
                cnt += 1 # 숫자 +1
        if cnt == 0 or cnt > l-2: # 만약 0개이거나 l-2개이상 >> 자음개수가 2개 이하이라면
            return # 돌아가기
        print(''.join(map(str, s))) # 만약 조건 성립이면 s에있는 원소들 붙여서 출력
        return
    for i in range(start, c): # 현재 위치 부터 끝까지 
        s.append(password[i]) # s에 현재위치의 패스워드 알파벳 넣기
        back(i+1) # 다음 위치로 이동
        s.pop() # 현재위치의 알파벳 빼기
    

l, c = map(int, input().split()) # 뽑아야 할 알파벳 수, 전체 문자열 길이
password = list(map(str, input().split())) # 문자열 리스트
password.sort() # 문자열 오름차순 정렬
s = [] # 문자열 받을 빈리스트
gather = ['a', 'e', 'i', 'o', 'u'] # 모음 리스트
back(0)