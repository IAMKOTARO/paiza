import re


def deployment(S:str) -> str:
    '''
    数字(文字列)の形もしくはその入れ子も考慮する
    '''
    if any(map(str.isdigit, S)):
        if len(S.replace(re.sub(r"\D", "", S), '')) == 3:
            times = re.sub(r"\D", "", S)
            return int(times) * S.replace(times, '').replace('(', '').replace(')', '')
        else:
            parentheses_left_string = S[:S.find('(')]
            parentheses_right_string = S[S.rfind(')')+1:]
            times = re.findall(r"\d+", parentheses_left_string)[-1]
            parentheses_left_string = parentheses_left_string.replace(times, '')
            parenthesis_inside_string = S[S.find('(')+1:S.rfind(')')]
            print(f'{parentheses_left_string} + {times} * {parenthesis_inside_string} + {parentheses_right_string}')
            return parentheses_left_string + int(times) * deployment(S=parenthesis_inside_string) + parentheses_right_string
    else:
        return S


S = input()
processed_S = ''
is_digit = S[0].isdigit()
for s in S:
    if s.isdigit() and not is_digit:
        is_digit = True
    if s.isalpha() and is_digit:
        is_digit = False
        processed_S += f'({s})'
    elif s in ['(', ')']:
        is_digit = False
        processed_S += s
    else:
        processed_S += s
stack = ''
full_string = ''
for s in processed_S:
    stack += s
    if stack.count('(') > 0 and stack.count(')') > 0 and stack.count('(') == stack.count(')'):
        print(stack)
        full_string += deployment(stack)
        stack = ''
print(full_string)
for i in range(97, 123):
    print(f'{chr(i)} {full_string.count(chr(i))}')
