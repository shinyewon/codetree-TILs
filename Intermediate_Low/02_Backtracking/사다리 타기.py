# 문제 링크: https://www.codetree.ai/missions/2/problems/ladder-game?&utm_source=clipboard&utm_medium=text
# 소요 시간: 2시간
# 미해결

n, m = map(int, input().split())
lines = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    lines[a].append(b)

# 한 사람의 결과(위치)를 반환


def go(person, lines):
    global n
    cur_b, cur_j = 1, person
    while (True):
        pass
        # 더이상 옆으로 이동할 수 없으면 break
        # cur_b보다 아래에 있는 가로줄 중 맨 위 가로줄로 이동
    return cur_j

# 게임의 결과를 반환


def ghostLeg(lines):
    global n
    global m
    result = [-1 for _ in range(n)]
    for person in range(1, n+1):
        pos = go(person, lines)
        result[pos] = person
    return result

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

# 가능한 가로줄 조합들을 모두 찾아준다.


def lineCmb(lines, cmb):
    global cmbs
    if len(lines) == 0:
        cmbs.append(cmb)
        return
    lineCmb(lines[1:], cmb)
    lineCmb(lines[1:], cmb.append(lines[0]))


init_res = ghostLeg(lines)
min_m = m               # 최소 가로줄 수

cmbs = []
lineCmb(lines, [])
for cmb in cmbs:
    if len(cmb) < min_m:
        res = checkRes(init_res, cmb)
        if res != []:
            min_m = len(cmb)

print(min_m)
