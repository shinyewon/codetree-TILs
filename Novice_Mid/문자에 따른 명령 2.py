# 문제 링크: https://www.codetree.ai/missions/5/problems/text-based-commands2?utm_source=clipboard&utm_medium=text
x, y = 0, 0
dir_num = 3

#     0.  1.  2. 3
dx = [1,  0, -1, 0]
dy = [0, -1,  0, 1]

dir_map = {'L': -1, 'R': 1}

for c in input():
    if c == 'F':
        x, y = x + dx[dir_num], y + dy[dir_num]
    else:
        dir_num = (dir_num + dir_map[c] + 4) % 4

print(x, y)
