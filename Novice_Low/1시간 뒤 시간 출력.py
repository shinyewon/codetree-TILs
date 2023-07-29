# 문제 링크: https://www.codetree.ai/missions/4/problems/print-one-hour-later?utm_source=clipboard&utm_medium=text
h, m = input().split(":")
h, m = int(h) + 1, int(m)
print("%d:%d" % (h, m))
