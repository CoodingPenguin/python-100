# 문제 16: 로꾸거

input_str = input()

new_str = ''
for i in range(len(input_str)):
    idx = -1 * (i+1)
    new_str += input_str[idx]

print(new_str)