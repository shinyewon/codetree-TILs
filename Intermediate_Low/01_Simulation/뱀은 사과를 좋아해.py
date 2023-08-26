# 문제 링크: https://www.codetree.ai/missions/2/problems/snake-loves-apples?&utm_source=clipboard&utm_medium=text
# 소요 시간: 1시간 30분
n, m, k = map(int, input().split())
grid = [
    ['.' for _ in range(n)]
    for _ in range(n)
]
for _ in range(m):
    x, y = map(int, input().split())
    grid[x-1][y-1] = "apple"
grid[0][0] = "head"
snake = [[0, 0]]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


dNum = {'U': 0, 'D': 1, 'R': 2, 'L': 3}
dis, djs = [-1, 1, 0, 0], [0, 0, 1, -1]
time = 0
out = False
for _ in range(k):
    d, p = input().split()
    p = int(p)
    # p만큼 이동
    for _ in range(p):
        time += 1
        new_i, new_j = snake[0][0] + dis[dNum[d]], snake[0][1] + djs[dNum[d]]
        if in_range(new_i, new_j):
            if grid[new_i][new_j] == "apple":
                grid[new_i][new_j] = "head"
                grid[snake[0][0]][snake[0][1]] = "body"
                snake = [[new_i, new_j]] + snake
            # 몸이 꼬이면
            elif grid[new_i][new_j] == "body" and not (new_i == snake[-1][0] and new_j == snake[-1][1]):
                out = True
                break
            else:
                grid[new_i][new_j] = "head"
                grid[snake[0][0]][snake[0][1]] = "."
                if len(snake) > 1:
                    grid[snake[0][0]][snake[0][1]] = "body"
                    grid[snake[-1][0]][snake[-1][1]] = '.'
                    snake = [[new_i, new_j]] + snake[:len(snake)-1]
                else:
                    snake = [[new_i, new_j]]
        else:
            out = True
            break
    if out:
        break

print(time)
