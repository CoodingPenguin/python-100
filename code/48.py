# 문제 48: 대소문자 바꿔서 출력하기

result = ''
for s in input():
    if s.islower():
        result += s.upper()
    else:
        result += s.lower()

print(result)