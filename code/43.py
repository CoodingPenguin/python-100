# 문제 43 : 10진수를 2진수로

num = int(input('10진수 : '))
result = ''

while num > 1:
    result = str(num % 2) + result
    num //= 2

result = str(num) + result
print('2진수 : ' + result)
