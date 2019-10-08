# 문제 8: 딕셔너리 키 이름 중복

d = {'height': 180, 'weight': 78, 'weight': 84, 'temparture': 36, 'eyesight': 1}

# 중복된 key값이 있을 경우 가장 최신의 value값으로 설정하여 하나로 만듦
print(d['weight'])      # 84