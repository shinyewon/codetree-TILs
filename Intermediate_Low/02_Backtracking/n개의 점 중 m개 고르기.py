# 문제 링크: https://www.codetree.ai/missions/2/problems/choose-m-out-of-n-points?utm_source=clipboard&utm_medium=text
n, m = map(int, input().split())
dots = [
    list(map(int, input().split()))
    for _ in range(n)
]


def distance(i, j):
    dis = (dots[i][0] - dots[j][0])**2 + (dots[i][1] - dots[j][1])**2
    return dis


squareDis = [
    [0 for _ in range(n)]
    for _ in range(n)
]
for i in range(n):
    for j in range(n):
        squareDis[i][j] = distance(i, j)

res = 20000


def dfs(n, m, dots, m_dots):
    global res
    if m == 0:
        dis = 0
        for i in range(len(m_dots)):
            for j in range(i+1, len(m_dots)):
                if squareDis[m_dots[i]][m_dots[j]] > dis:
                    dis = squareDis[m_dots[i]][m_dots[j]]
        if dis < res:
            res = dis
    for i in range(len(dots)):
        dfs(n, m-1, dots[i+1:], m_dots+[i+n-len(dots)])


dfs(n, m, dots, [])
print(res)
