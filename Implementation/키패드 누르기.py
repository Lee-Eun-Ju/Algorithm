import numpy as np

def solution(numbers, hand):
    answer = []   
    pad = {1:(1,1), 2:(1,2), 3:(1,3), 4:(2,1), 5:(2,2), 6:(2,3), 7:(3,1), 8:(3,2), 9:(3,3), "*":(4,1), 0:(4,2), "#":(4,3)}

    for num in numbers:
        if num in [1,4,7,"*"]:
            answer.append("L")
            
        elif num in [3,6,9,"#"]:
            answer.append("R")
            
        else:
            # 이전 왼쪽엄지값, 오른쪽엄지값
            if "L" not in answer:
                l = "*"
            else:
                which_left = np.where(np.array(answer)=='L')[0][-1]
                l = numbers[which_left]
            if "R" not in answer:
                r = "#"
            else:
                which_right = np.where(np.array(answer)=='R')[0][-1]
                r = numbers[which_right]
            
            # 키패드 거리
            distance_left = abs((pad[l][0]-pad[num][0])) + abs((pad[l][1]-pad[num][1]))
            distance_right = abs((pad[r][0]-pad[num][0])) + abs((pad[r][1]-pad[num][1]))
            
            # 어떤 엄지로 키패드를 누를까?
            if (distance_left == distance_right)&(hand=="right"):
                answer.append("R")
            elif (distance_left == distance_right)&(hand=="left"):
                answer.append("L")
            elif distance_left > distance_right:
                answer.append("R")
            elif distance_left < distance_right:
                answer.append("L")
            else:
                answer.append(" ")
                
    answer = "".join(answer)
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
solution(numbers,hand)