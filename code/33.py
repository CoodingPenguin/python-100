# 문제 33: 거꾸로 출력하기

num = [int(x) for x in input().strip().split()]
num.reverse()

for x in num:
    print(x, end=' ')