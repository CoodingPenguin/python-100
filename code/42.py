# 문제 42: 2020년
import datetime

int_day = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
           4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}


def find_day(month, day):
    input_day = datetime.date(2020, month, day)

    return int_day[input_day.isoweekday()]


input_date = [int(x) for x in input('2020년 a월 b일을 띄어쓰기로 띄워서 입력하시오 : ').split()]
print(find_day(input_date[0], input_date[1]))
