# 공백없이 입력받은 문자를 나누어야 할 때
s = list(map(int, input()))

result=0
for i in s:
    if result==0 or result==1:
        result += i
    elif i==0 or i==1:
        result += i
    else:
        result *= i
print(result)