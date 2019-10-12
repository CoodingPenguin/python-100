# 문제 20: 몫과 나머지

input_str = input().split()
dividend = int(input_str[0])
divisor = int(input_str[1])

print(dividend//divisor, dividend%divisor, sep=' ')