# 문제 링크: https://www.codetree.ai/missions/2/problems/beautiful-number?utm_source=clipboard&utm_medium=text
n = int(input())
cnt = 0


def dfs(curr_pos):
    global cnt
    if curr_pos == n:
        cnt += 1
        return
    for i in range(1, 5):
        if curr_pos+i <= n:
            dfs(curr_pos+i)
    return


dfs(0)
print(cnt)
