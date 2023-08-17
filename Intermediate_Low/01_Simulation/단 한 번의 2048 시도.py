# 미해결
# 문제 링크: https://www.codetree.ai/missions/2/problems/one-trial-of-2048-game?utm_source=clipboard&utm_medium=text
# 소요 시간: 2시간 30분
nums = [
    list(map(int, input().split()))
    for _ in range(4)
]
d = input()
nums2 = [
    []
    for _ in range(4)
]

if d == 'U' or d == 'D':
    numsji = [
        [0 for _ in range(4)]
        for _ in range(4)
    ]
    for i in range(4):
        for j in range(4):
            numsji[j][i] = nums[i][j]
    nums = numsji

# 밀기
for i in range(4):
    for j in range(4):
        if nums[i][j] != 0:
            nums2[i].append(nums[i][j])

if d == 'L' or d == 'U':
    # 더하기
    for i in range(4):
        l = len(nums2[i])
        if l >= 2:
            last_num = nums2[i][0]
        else:
            continue
        for j in range(1, l):
            if nums2[i][j] == last_num:
                nums2[i][j-1] = last_num * 2
                nums2[i][j] = 0
                last_num = -1
            else:
                last_num = nums2[i][j]

    if d == 'U':
        # 밀기
        nums3 = [
            []
            for _ in range(4)
        ]
        for i in range(4):
            for j in range(len(nums2[i])):
                if nums2[i][j] != 0:
                    nums3[i].append(nums2[i][j])
        nums2 = nums3

        numsij = [
            [0 for _ in range(4)]
            for _ in range(4)
        ]
        for i in range(4):
            for j in range(len(nums2[i])):
                numsij[j][i] = nums2[i][j]
        nums2 = numsij
        # 출력
        for i in range(4):
            for j in range(4):
                print(nums2[i][j], end=" ")
            print()
    if d == 'L':
        for i in range(4):
            cnt = 0
            for j in range(len(nums2[i])):
                if nums2[i][j] != 0:
                    print(nums2[i][j], end=" ")
                    cnt += 1
            for _ in range(4-cnt):
                print(0, end=" ")
            print()


elif d == 'R' or d == 'D':
    # 더하기
    for i in range(4):
        l = len(nums2[i])
        if l >= 2:
            last_num = nums2[i][l-1]
        else:
            continue
        for j in range(l-2, -1, -1):
            if nums2[i][j] == last_num:
                nums2[i][j+1] = last_num * 2
                nums2[i][j] = 0
                last_num = -1
            else:
                last_num = nums2[i][j]

    for i in range(4):
        print(nums2[i])
    if d == 'D':
        # 밀기
        for i in range(4):
            for j in range(4):
                if nums[i][j] != 0:
                    nums2[i].append(nums[i][j])
        # 행렬변환
        numsij = [
            [0 for _ in range(4)]
            for _ in range(4)
        ]
        for i in range(4):
            for j in range(len(nums2[i])):
                print("ij", i, j)
                numsij[j][i] = nums2[i][j]
        nums2 = numsij

    for i in range(4):
        print(nums2[i])

    # 출력
    for i in range(4):
        cnt = 0
        for j in range(len(nums2[i])):
            if nums2[i][j] != 0:
                cnt += 1
        for _ in range(4-cnt):
            print(0, end=" ")
        for j in range(len(nums2[i])):
            if nums2[i][j] != 0:
                print(nums2[i][j], end=" ")
        print()
