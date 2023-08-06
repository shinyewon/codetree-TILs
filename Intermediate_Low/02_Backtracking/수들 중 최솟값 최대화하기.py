# 문제 링크: https://www.codetree.ai/missions/2/problems/maximin-of-numbers?utm_source=clipboard&utm_medium=text
n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

res = 0


def dfs(row, visited_col, colored):
    global res
    if row == n:
        if min(colored) > res:
            res = min(colored)
    for i in range(n):
        can_color = True
        for col in visited_col:
            if i == col:
                can_color = False
        if can_color:
            dfs(row+1, visited_col+[i], colored+[arr[row][i]])


dfs(0, [], [])
print(res)
