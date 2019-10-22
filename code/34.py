# 문제 34: sort 구현하기
# 답안 참고 : sort함수 사용

height = [int(x) for x in input('입력 : ').strip().split()]

prev = height[0]
result = 'YES'
for idx in range(1, len(height)):
    if height[idx] <= prev:
        result = 'NO'
        break
    else:
        prev = height[idx]

print('출력 :', result)