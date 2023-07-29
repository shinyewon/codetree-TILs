# 문제 링크: https://www.codetree.ai/missions/5/problems/add-all-the-numbers-on-the-path?utm_source=clipboard&utm_medium=text
n, t = tuple(map(int, input().split()))
cmd = input()
arr = [
    [0] * n
    for _ in range(n)
]
for i in range(n):
    arr[i] = list(map(int, input().split()))

dis, djs = [-1, 0, 1, 0], [0, 1, 0, -1]
dir_num = 0
i, j = n//2, n//2
sum = arr[i][j]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


for c in cmd:
    if c == 'F':
        ni, nj = i + dis[dir_num], j + djs[dir_num]
        if in_range(ni, nj):
            i, j = ni, nj
            sum += arr[i][j]
    elif c == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    else:
        dir_num = (dir_num + 1) % 4

print(sum)
