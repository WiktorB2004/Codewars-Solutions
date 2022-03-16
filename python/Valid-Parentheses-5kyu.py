#1 SOLUTION - refactored version of the first one
def valid_parentheses(str):
    count = 0
    for char in str:
        if char == '(': count += 1
        if char == ')': count -= 1
        if count < 0: return False
    return True if count == 0 else False

#2 SOLUTION
import re
def valid_parentheses(str):
    str = re.findall('[(,)]', str)
    if str:
        if str[0] == ')' or len(str) == 1:
            return False
        o = 0
        c = 0
        for char in str:
            if char == '(':
                o += 1
            elif char == ')':
                c += 1
            if o - c < 0:
                return False
        if o > c:
            return False
    return True