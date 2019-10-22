# 문제 35: Factory 함수 사용하기
# 함수형 프로그래밍 공부

def one(n):
    def two(value):
        result = value**n
        return result
    return two

a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))