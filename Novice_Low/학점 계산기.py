# 문제 링크: https://www.codetree.ai/missions/4/problems/credit-calculator?utm_source=clipboard&utm_medium=text
n = int(input())
arr = list(map(float, input().split()))

sum_val = 0
for i in range(n):
    sum_val += arr[i]

ave = sum_val / n
print("%.1f" % ave)
if ave >= 4.0:
    print("Perfect")
elif ave >= 3.0:
    print("Good")
else:
    print("Poor")
