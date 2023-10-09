# 문제 링크: https://www.codetree.ai/missions/2/problems/ladder-game?&utm_source=clipboard&utm_medium=text
# 소요 시간: 4시간(해설 참조)
# dfs에서 배열을 parameter로 전달할 때에는 복사해서 전달하도록 하자!

n, m = tuple(map(int, input().split()))
lines = list()
for _ in range(m):
    a, b = tuple(map(int, input().split()))
    lines.append((b, a))
lines.sort()


def go(person, lines):
    '''한 사람의 결과(위치)를 반환'''
    global n
    cur_b, cur_j = 1, person
    while (True):
        found = False
        for line in lines:
            if line[0] >= cur_b and (line[1] == cur_j or line[1] == cur_j-1):
                found = True
                cur_b = line[0] + 1
                if line[1] == cur_j:
                    cur_j += 1
                else:
                    cur_j -= 1
                break
        if not found:
            break
    return cur_j


def ghostLeg(lines):
    '''게임의 결과를 반환'''
    global n
    global m
    result = [-1 for _ in range(n)]
    for person in range(1, n+1):
        pos = go(person, lines)
        result[pos-1] = person
    return result


def lineCmb(i, cmb):
    '''가능한 가로줄 조합들을 모두 찾아준다.'''
    global cmbs
    if i == m:
        cmbs.append(cmb)
        return
    cmb.append(lines[i])
    lineCmb(i+1, cmb[:])
    cmb.pop()
    lineCmb(i+1, cmb[:])


init_res = ghostLeg(lines)
min_m = m  # 최소 가로줄 수


cmbs = list()
lineCmb(0, [])

for cmb in cmbs:
    if len(cmb) < min_m and init_res == ghostLeg(cmb):
        min_m = len(cmb)

print(min_m)
