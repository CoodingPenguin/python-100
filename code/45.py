# 문제 45: time함수 사용하기
import time

minutes = time.time()//60
hours = minutes//60
days = hours//24
years = days//365

print(1970 + int(years))