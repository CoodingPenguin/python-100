# 문제 18: 평균 점수

input_str = input().split()
subjects = []
for i in input_str:
    subjects.append(int(i))

print(sum(subjects)//len(subjects))