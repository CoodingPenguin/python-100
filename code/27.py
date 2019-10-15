# 문제 27: 딕셔너리 만들기

names = input().split()
scores = [int(x) for x in input().split()]

tables = {names[i]:scores[i] for i in range(len(names))}
print(tables)