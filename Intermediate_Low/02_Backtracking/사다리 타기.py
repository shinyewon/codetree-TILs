# 문제 링크: https://www.codetree.ai/missions/2/problems/ladder-game?&utm_source=clipboard&utm_medium=text
# 소요 시간: 3시간
# 미해결

n, m = map(int, input().split())
lines = [
    [0 for _ in range(n+1)]
    for _ in range(m+1)
]
for _ in range(m):
    a, b = map(int, input().split())
    lines[b][a] = 1
    lines[b][a+1] = 1

# 한 사람의 결과(위치)를 반환


def go(person, lines):
    global n
    cur_i, cur_j = 1, person
    for i in range(1, n+1):
        if lines[i][cur_j] == 1:
            if 0 < cur_j - 1 and lines[i][cur_j-1] == 1:
                cur_j -= 1
            elif cur_j + 1 <= n and lines[i][cur_j+1] == 1:
                cur_j += 1
    return cur_j

# 게임의 결과를 반환


def ghostLeg(lines):
    global n
    global m
    result = [-1 for _ in range(n)]
    for person in range(1, n+1):
        pos = go(person, lines)
        result[pos-1] = person
    return result


'''
# 게임 결과의 일치 여부 반환
def checkRes(init_res, lines):
    global n
    global m
    result = [-1 for _ in range(n)]
    isSame = True
    for person in range(1, n+1):
        pos = go(person, lines)
        result[pos] = person
        if result[pos] != init_res[pos]:
            isSame = False
            break
    return isSame
'''
# 가능한 가로줄 조합들을 모두 찾아준다.


def lineCmb(lines, i, cnt, cmb):
    global cmbs
    found = False
    next_i = 1
    if cnt == m:
        cmbs.append(cmb)
        return
    for b in range(i, m+1):
        for j in range(1, n+1):
            if lines[b][j] == 1:
                found = True
                next_i = b
                lines[0][0] += 1
                lineCmb(lines, next_i, cnt+1, lines)
                lines[0][0] -= 1
                lines[b][j] = 0
                if j-1 > 0 and lines[b][j-1] == 1:
                    lines[b][j-1] = 0
                else:
                    lines[b][j+1] = 0
                break
        if found:
            break
    lineCmb(lines, next_i, cnt+1, lines)


init_res = ghostLeg(lines)
min_m = m  # 최소 가로줄 수

cmbs = []
lineCmb(lines, 1, 0, [])
print(cmbs)
for cmb in cmbs:
    if cmb[0][0] < min_m:
        if init_res == ghostLeg(cmb):
            min_m = cmb[0][0]

print(min_m)
