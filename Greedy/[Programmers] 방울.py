# 방울

from itertools import accumulate

def solution(bell):
    
    # (빨간색)1→-1, (초록식)2→1
    bell = [-1 if i==1 else 1 for i in bell]
    
    # accumulate : 누적합 계산(초록색과 빨간색의 차이)
    # [0] : 구간 설정을 위해
    sum_bell = accumulate([0] + bell)
    
    # dictonary : key-value
    coors_start = {}
    coors_end = {}
    for i,x in enumerate(sum_bell):
        if x not in coors_start:
            coors_start[x] = i # -1이 있던 자리
        coors_end[x] = i # -1과 같은 숫자 중 가장 먼 자리로 갱신
        
    answer = max(coors_end[x]-coors_start[x] for x in coors_start)
    return answer