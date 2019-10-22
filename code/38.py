# 문제 38: 호준이의 아르바이트
# 답안 나중에 다시 참고 (조금 이상함)

parsing = input('점수입력 : ').strip().split()
students = [int(x) for x in parsing]
scores = set(students)
best3 = set()

for i in range(3):
    max_score = max(scores)
    best3.add(max(scores))
    scores.remove(max_score)

total = 0
for score in best3:
    total += students.count(score)

print('출력 :', total)