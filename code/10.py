# 문제 10: 별 찍기

N = int(input())

for i in range(1, N+1):
    print(" "*(N-i), "*"*(i*2 - 1), sep='')