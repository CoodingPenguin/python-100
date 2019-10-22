# 문제 40: 놀이동산에 가자

limit = int(input())
count = int(input())

sum = 0
result = 0
for p in range(count):
    sum += int(input())
    if sum > limit:
        result = p
        break

print(result)
