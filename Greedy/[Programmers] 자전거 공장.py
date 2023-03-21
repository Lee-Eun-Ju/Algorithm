# 자전거 공장

def solution(cost, order):
    
    #아이디어: 모든 생산을 골고루 배치
    #이때 주문이 앞쪽에 몰린 경우 골고루 배치 불가능
    #즉, 뒷쪽의 주문량이 많은 경우 앞쪽과 합쳐줌으로써 골고루 배치하도록 풀이
    
    #PART1. order → 구간별 생산양으로 변경
    order.sort()
    _order = [order[0]]
    for i, (m,n) in enumerate(order[1:]):
        # m: order[1], order[i]: order[0]
        _order.append([m-order[i][0],n])
        
    
    #PART2. 뒷쪽 주문이 많은 경우 
    stack = []
    for m,n in _order:
        while stack: #리스트의 데이터가 없을 때까지 while문
            _m, _n = stack[-1] #앞쪽 주문 중 가장 최근 주문
            if _m/_n < m/n: # 앞쪽주문이 더 많은 경우 정지
                break
            stack.pop() #뒷쪽 주문이 많은 경우 현재 가장 최근 주문 추출
            m, n = m+_m, n+_n #뒷쪽 주문과 결합
        stack.append([m,n])
    
    #PART3. 비용 계산
    answer = 0
    for m,n in stack:
        p_prev =0
        for t,p in cost:
            if m*t>=n: #정해진수량의기준*개월 >= 주문량이면 break
                break
            answer += (n-m*t)*(p-p_prev) #넘긴갯수*차액
            p_prev = p
            
    return answer