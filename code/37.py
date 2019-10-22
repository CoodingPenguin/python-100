# 문제 37: count 사용하기
# 답안 참고 : map과 리스트 사용

votes = input().split()
candidates = dict.fromkeys(set(votes), 0)

MAX = 0
winner = ''
for person in candidates.keys():
    candidates[person] = votes.count(person)
    if votes.count(person) > MAX:
        MAX = votes.count(person)
        winner = person

print('{0}(이)가 총 {1}표로 반장이 되었습니다.'.format(winner, MAX))