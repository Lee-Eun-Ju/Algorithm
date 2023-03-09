import itertools
import numpy as np

# input
n = int(input())
coin = list(map(int, input().split()))

# coin 조합
coin_comb = []
for i in range(1,len(coin)+1):
    x = list(itertools.combinations(coin,i))
    for j in x:
        coin_comb.append(sum(j))

# 결과 (만들 수 있을 경우 -> 1)
result = [0]*1000
for i in coin_comb:
    result[i] =1

for i in range(1,len(result)):
    if result[i]==0:
        print(i)
        break