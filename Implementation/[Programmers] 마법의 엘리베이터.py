# 마법의 엘리베이터 (Answer)

def solution(storey):
    # 재귀함수 중단 조건
    if storey<= 1:
        return storey
    
    # divmod : 몫과 나머지 동시 도출
    # storey의 자릿수를 10의 단위로 나누어준다
    q, r = divmod(storey, 10)
    
    # 재귀함수
    answer = min(solution(q)+r, solution(q+1)+(10-r))
    
    return answer