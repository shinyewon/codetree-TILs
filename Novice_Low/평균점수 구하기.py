# 문제 링크: https://www.codetree.ai/missions/4/problems/print-average?utm_source=clipboard&utm_medium=text
scores = list(map(float, input().split()))
sum_val = 0
for score in scores:
    sum_val += score
ave = sum_val / 8
print("%.1f" % ave)
