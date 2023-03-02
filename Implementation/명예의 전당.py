k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]

answer = []
for j in range(1,k+1):
    answer.append(min(score[0:j]))

for i in range(k+1,len(score)+1):
    data = sorted(score[0:i], reverse=True)
    answer.append(data[k-1])

answer