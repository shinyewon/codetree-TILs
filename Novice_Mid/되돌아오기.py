# 문제 링크: https://www.codetree.ai/missions/5/problems/come-back?utm_source=clipboard&utm_medium=text
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
dir_map = {'N': 0, 'E': 1, 'W': 2, 'S': 3}
x, y = 0, 0
time = 0
isSpos = False
n = int(input())

for _ in range(n):
    c_dir, num = input().split()
    num = int(num)
    dir_num = dir_map[c_dir]
    for _ in range(num):
        x, y = x + dxs[dir_num], y + dys[dir_num]
        time += 1
        if x == 0 and y == 0:
            isSpos = True
            break
    if isSpos:
        break

if isSpos:
    print(time)
else:
    print(-1)
