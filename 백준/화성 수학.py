# 브론즈 2

import sys
sys.stdin = open("E:/Algorithms_Python/백준/input.txt", "r")

arr = [input().split(' ') for _ in range(int(input()))]
result_arr = []

for line in arr:
    sum = float(line[0])
    for idx in range(1,len(line)):
        operator = line[idx]
        if(operator == '@'): sum *= 3
        elif(operator == '%'): sum += 5
        elif(operator == '#'): sum -= 7
    result_arr.append(f'{sum : .2f}')

for result in result_arr:
    print(result)
# print('\n'.join(result))