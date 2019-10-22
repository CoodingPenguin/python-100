# 문제 31: 파이썬 자료형의 복잡도
l = [1, 2, 3, 4]
i = 3
a, b = 2, 4

# slicing 빼고 나머지 시간복잡도 O(1)
l[i]            # indexing
l.append(5)     # append 함수
l[a:b]          # slicing : indexing을 b-a+1번 해야되니까 / O(n)
l.pop()         # pop 함수
l.clear()       # clear 함수