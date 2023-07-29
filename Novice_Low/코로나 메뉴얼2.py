# 문제 링크: https://www.codetree.ai/missions/4/problems/covid-manual2?utm_source=clipboard&utm_medium=text
clinic = [0] * 4
for i in range(3):
    cold, temp = input().split()
    temp = int(temp)
    if cold == 'Y':
        if temp >= 37:
            clinic[0] += 1
        else:
            clinic[2] += 1
    else:
        if temp >= 37:
            clinic[1] += 1
        else:
            clinic[3] += 1

for num in clinic:
    print(num, end=" ")
if clinic[0] >= 2:
    print('E')
