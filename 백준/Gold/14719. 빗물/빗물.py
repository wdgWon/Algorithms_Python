h, w = map(int, input().split())
blocks = [int(num) for num in input().split()]
area = [[0] * w for _ in range(h)]
count = 0

for i in reversed(range(h)):
    for j in range(w):
        if blocks[j]:
            area[i][j] = 1
            blocks[j] -= 1

for line in area:
    mode = False
    tmp_count = 0
    for block in line:
        if mode == True and block == 0:
            tmp_count += 1
        elif block == 1:
            mode = True
            count += tmp_count
            tmp_count = 0

print(count)