# 브론즈 3

import sys
sys.stdin = open("E:/Algorithms_Python/백준/input.txt", "r")

current, required = [input() for _ in range(2)]
hour, minute = map(int, current.split(' '))
required = int(required)

hour, minute = (hour + (minute + required) // 60) % 24, (minute + required) % 60
print(hour, minute)
# current_time = time(int(hour), int(minute))
# required_time = time(0, int(required))
# result = current_time + required_time

