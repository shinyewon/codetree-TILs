# 문제 링크: https://www.codetree.ai/missions/2/problems/sequential-movement-of-stacked-numbers?&utm_source=clipboard&utm_medium=text
# 소요 시간: 1시간 38분
n, m = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
nums = list(map(int, input().split()))
dis, djs = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]


def in_range(i, j):
    return i >= 0 and i < n and j >= 0 and j < n


def findPos(num):  # 움직일 숫자의 위치 찾기
    index = []
    for i in range(n):
        for j in range(n):
            if type(board[i][j]) == list:
                for k in range(len(board[i][j])):
                    if board[i][j][k] == num:
                        index = [i, j, k]
                        return index
            elif board[i][j] == num:
                index = [i, j]
                return index


for num in nums:
    index = findPos(num)
    # 인접한 숫자 중 가장 큰 값 찾기
    max_v = 0
    max_i = []
    for di, dj in zip(dis, djs):
        new_i, new_j = index[0] + di, index[1] + dj
        if in_range(new_i, new_j) and board[new_i][new_j] is not None:
            if type(board[new_i][new_j]) == list:
                for k in range(len(board[new_i][new_j])):
                    if board[new_i][new_j][k] > max_v:
                        max_v = board[new_i][new_j][k]
                        max_i = [new_i, new_j]
            elif board[new_i][new_j] > max_v:
                max_v = board[new_i][new_j]
                max_i = [new_i, new_j]
    # 움직이기
    if len(max_i) > 0:
        if len(index) == 2:  # 이동하는 숫자가 한 개면
            board[max_i[0]][max_i[1]] = [num] + ([board[max_i[0]][max_i[1]]] if type(
                board[max_i[0]][max_i[1]]) == int else board[max_i[0]][max_i[1]])
            board[index[0]][index[1]] = None
        else:
            board[max_i[0]][max_i[1]] = board[index[0]][index[1]][:index[2]+1] + \
                ([board[max_i[0]][max_i[1]]] if type(board[max_i[0]]
                 [max_i[1]]) == int else board[max_i[0]][max_i[1]])
            board[index[0]][index[1]] = (board[index[0]][index[1]][index[2]+1:] if len(
                board[index[0]][index[1]][index[2]+1:]) > 0 else None)

for i in range(n):
    for j in range(n):
        if type(board[i][j]) != list:
            print(board[i][j])
        else:
            for k in range(len(board[i][j])):
                print(board[i][j][k], end=" ")
            print()
