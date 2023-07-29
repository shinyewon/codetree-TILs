# 문제 링크: https://www.codetree.ai/missions/4/problems/reaching-specific-number?utm_source=clipboard&utm_medium=text
arr = input().split()
sum = 0
ave = 0
for i in range(10):
    arr[i] = int(arr[i])
    if arr[i] < 250:
        sum += arr[i]
        ave = sum / (i+1)
    else:
        break
print("%d %.1f" % (sum, ave))
