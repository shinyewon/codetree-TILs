# 문제 링크: https://www.codetree.ai/missions/2/problems/min-num-of-jumps?utm_source=clipboard&utm_medium=text
n = int(input())
jumps = list(map(int, input().split()))

res = 10


def dfs(n, jumps, pos, cnt):
    global res
    if n <= 1:
        if cnt < res:
            res = cnt
        return
    for i in range(1, jumps[pos]+1):
        dfs(n-i, jumps, pos+i, cnt+1)


dfs(n, jumps, 0, 0)
if res != 10:
    print(res)
else:
    print(-1)
