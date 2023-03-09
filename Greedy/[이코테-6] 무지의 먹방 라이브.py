food_times = list(map(int,input().split()))
k = int(input())


## 효율성 측면에서 다시 생각해보기!
def solution(food_times, k):
    
    result = 0 # 음식 먹은 횟수 (흐른 시간)
    answer = -1 # 언제부터 다시 먹기 시작해야하는 가?
    while sum(food_times)!=0:
        for i in range(len(food_times)):
            if food_times[i]!=0:
                food_times[i]-=1
                result += 1
            if result==(k+1): 
                answer=i+1
                break
        if result==(k+1): 
            break
        
    return answer