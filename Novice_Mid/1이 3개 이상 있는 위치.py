# 문제 링크: https://www.codetree.ai/missions/5/problems/place-more-than-3-ones?utm_source=clipboard&utm_medium=text
n = int(input())
arr = [[0]*n] * n
for i in range(n):
    arr[i] = list(map(int, input().split()))


def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y < n


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
cnt_1 = 0
cnt_cell = 0
for i in range(n):
    for j in range(n):
        for dx, dy in zip(dxs, dys):
            # (x, y)에서 dir_num 방향으로 한 칸 이동했을 때의 위치 구하기
            nx, ny = i + dx, j + dy

            if in_range(nx, ny, n) == True and arr[nx][ny] == 1:
                cnt_1 += 1
        if cnt_1 >= 3:
            cnt_cell += 1
        cnt_1 = 0

print(cnt_cell)
