def solution(numbers, hand):
    keypad = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9: [2,2], 0: [3,1]}
    left = [3, 0]
    right = [3, 2]
    result = ''
    
    for number in numbers:
        if number % 3 == 1:
            result += 'L'
            left = keypad[number]
        elif number % 3 == 0 and number != 0:
            result += 'R'
            right = keypad[number]
        else:
            dis_l = abs(keypad[number][0] - left[0]) + abs(keypad[number][1] - left[1])
            dis_r = abs(keypad[number][0] - right[0]) + abs(keypad[number][1] - right[1])
            
            if dis_l > dis_r or (hand == 'right' and dis_l == dis_r):
                result += 'R'
                right = keypad[number]
            else:
                result += 'L'
                left = keypad[number]
                
                
    
    return result
    