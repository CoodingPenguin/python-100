# 문제 46: str 자료형의 응용
nums = range(1, 101)
string = ''
result = 0

for n in nums:
    string += str(n)

for s in string:
    result += int(s)

print(result)