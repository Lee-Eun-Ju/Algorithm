import itertools

n, m = map(int, input().split())
k = list(map(int,input().split()))

result = 0
for i in k:
    result_i = []  
    for j in k:
        if j!=i:
            result_i.append(j)
    result += len(result_i)

print(result/2)