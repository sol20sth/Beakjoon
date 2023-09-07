def solution(gems):  # 투포인트
    answer = [0, len(gems)]   # 시작, 끝 정답리스트
    gem_dict = {gems[0] : 1}  # 보석이름, 개수
    n = len(set(gems))    # 보석의 종류 개수
    left, right = 0, 0  # 왼쪽 오른쪽   [left:right+1] 을 탐색하여서 보석이 모두 들어있는 범위들 찾기
    while right>=left:  # 왼쪽이 오른쪽보다 커지면 끝ㅌ내기
        if len(gem_dict) != n: # 보석이 모두 안모였으면
            right += 1 # 오른쪽을 한칸이동 : 구역 변경
            if right == len(gems): # 리스트 범위를 벗어나면 끝내기 
                break
            if gems[right] in gem_dict: # 딕셔너리안에 오른쪽 보석이 있으면 해당 보석개수 +1
                gem_dict[gems[right]] += 1
            else:  # 없으면 추가  없었다 있었으니 1
                gem_dict[gems[right]] = 1
        else:  # 보석이 모두 모였으면 최소값을 찾아야함
            if right - left < answer[1] - answer[0]:  # 보석이 모였으니 정답에 들어가있는 최소값과 비교
                # <= 안되는 이유는 범위를 오른쪽으로 이동시키며 비교하는 중이기 때문에 같은 범위라면 먼저 들어간 정답이
                # 더 왼쪽이기 떄문에 
                answer = [left, right] # 정답 재설정       
            else:  # 최소값이 아니면
                gem_dict[gems[left]] -= 1 # 왼쪽의 보석을 1개빼버리기 : 왼쪽의 구역을 한칸오른쪽으로 이동시킬예정이니 보석도 1개줄어듬
                if gem_dict[gems[left]] == 0: # 0개가 된다면 딕셔너리에 해당 보석을 없애버리기 : 없애야 len(gen_dict)을 확인가능
                    del gem_dict[gems[left]] 
                left += 1 # 왼쪽포인트 오른쪽으로 1칸
    return [answer[0]+1, answer[1]+1]  # 1번부터 시작했으니 +1
