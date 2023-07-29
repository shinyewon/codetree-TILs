# 문제 링크: https://www.codetree.ai/missions/5/problems/move-in-direction?utm_source=clipboard&utm_medium=text
n = int(input())
x, y = 0, 0
dx = {'N': 0, 'E': 1, 'S': 0, 'W': -1}
dy = {'N': 1, 'E': 0, 'S': -1, 'W': 0}
for i in range(n):
    direction, dis = input().split()
    dis = int(dis)
    x, y = x + dx[direction] * dis, y + dy[direction] * dis
print(x, y)
