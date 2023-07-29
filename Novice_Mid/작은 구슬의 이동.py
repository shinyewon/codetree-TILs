# 문제 링크: https://www.codetree.ai/missions/5/problems/small-marble-movement?utm_source=clipboard&utm_medium=text
n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r)-1, int(c)-1
d_num = {'U': 2, 'R': 0, 'L': 3, 'D': 1}
dir_num = d_num[d]

# R  D   U  L
dis, djs = [0, 1, -1, 0], [1, 0, 0, -1]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


for _ in range(t):
    nx, ny = r + dis[dir_num], c + djs[dir_num]
    if not in_range(nx, ny):  # check whether position is out of grid
        dir_num = 3 - dir_num  # change direction
    else:
        r, c = nx, ny
print(r+1, c+1)
