# 문제 10: 별 찍기

N = int(input())

for row in range(N):
    for col in range(N+row):
        if col < N-row-1:
            print(' ', end='')
        else:
            print('*', end='')
    print()