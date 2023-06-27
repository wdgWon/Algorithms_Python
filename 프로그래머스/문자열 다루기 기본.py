import re
def solution(s):
    if((len(s) == 4 or len(s) == 6) and not re.compile('\D').search(s)):
        return True
    else:
        return False