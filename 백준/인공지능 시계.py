# 브론즈 4

import sys
sys.stdin = open("E:/Algorithms_Python/백준/input.txt", "r")

current, required = [input() for _ in range(2)]
hour, minute, second = map(int, current.split(' '))
required = int(required)

seconds = (second + required) // 60
minutes = (minute + seconds) // 60
hours = hour + minutes

hour, minute, second = hours % 24, (minute + seconds) % 60, (second + required) % 60
print(hour, minute, second)