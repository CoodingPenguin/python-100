# 문제 41: 소수 판별
import math

# 방법 1 : 2부터 N-1까지


def isPrimeNumber1(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# 방법 2 : 에라토스테네스 접근


def isPrimeNumber2(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


input_num = int(input('숫자를 입력하시오 : '))

print('소수판별기1 :', isPrimeNumber1(input_num))
print('소수판별기2 :', isPrimeNumber2(input_num))
