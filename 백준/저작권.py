# 브론즈 3

import sys
sys.stdin = open("E:/Algorithms_Python/백준/input.txt", "r")

average, ceil_value = map(int, input().split(' '))

print(average * (ceil_value-1) + 1)