import math
def solution(wallpaper):
    lux, luy = [math.inf] * 2
    rdx, rdy = [-math.inf] * 2
    
    for x_idx, y_str in enumerate(wallpaper):
        y_first = y_str.find("#")
        y_last = y_str.rfind('#')
        
        if y_first >= 0:
            lux = min(lux, x_idx)
            rdx = max(rdx, x_idx + 1)
        
            luy = min(luy, y_first)
            rdy = max(rdy, y_last + 1)
    
    return [lux, luy, rdx, rdy]
        