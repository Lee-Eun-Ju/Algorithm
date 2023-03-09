# 입력
s = list(map(int, input()))

group = 0
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        pass
    else:
        group+=1

# 출력
if group%2==1:
    print((group+1)/2)
else:
    print(group/2)