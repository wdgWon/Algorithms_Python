import datetime

def switch(time):
    return ["FRI","SAT","SUN","MON","TUE","WED","THU"][time % 7]
    
def solution(a, b):
    d = datetime.date(2016, a, b) - datetime.date(2016, 1, 1)
    return switch(d.days)