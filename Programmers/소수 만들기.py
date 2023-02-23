nums = [1,2,7,6,4]

import itertools
data = list(itertools.combinations(nums,3))

result = []
for sum_3 in data:
    result.append(sum_3[0] +sum_3[1] +sum_3[2] )

not_answer = []
for i in result:
    for j in range(2,i):
        if i%j ==0:
            not_answer.append(i)
            break

answer = [k for k in result if k not in not_answer]