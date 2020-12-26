# 문제 53: 괄호 문자열

stack1 = []
stack2 = []
stack3 = []

try:
    for i in input():
        if i == '(':
            stack1.append('(')
        elif i == '{':
            stack2.append('{')
        elif i == '[':
            stack3.append('[')
        elif i == ')':
            stack1.pop()
        elif i == '}':
            stack2.pop()
        elif i == ']':
            stack3.pop()
        else:
            print('잘못된 입력입니다.')
            exit(0)

    if not stack1 and not stack2 and not stack3:
        print('YES')
    else:
        print('NO')

except IndexError:
    print('NO')
