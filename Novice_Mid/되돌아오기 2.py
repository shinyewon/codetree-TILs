# 문제 링크: https://www.codetree.ai/missions/5/problems/come-back-2?utm_source=clipboard&utm_medium=text
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0
x, y = 0, 0
time = 0
isSpos = False
cmd = input()

for c in cmd:
    if c == 'F':
        x, y = x + dxs[dir_num], y + dys[dir_num]
    elif c == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    else:
        dir_num = (dir_num + 1) % 4
    time += 1
    if x == 0 and y == 0:
        isSpos = True
        break

if isSpos:
    print(time)
else:
    print(-1)
