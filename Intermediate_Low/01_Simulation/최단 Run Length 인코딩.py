# 문제 링크: https://www.codetree.ai/missions/2/problems/shortest-run-length-encoding?utm_source=clipboard&utm_medium=text
# 소요 시간: 27분
A = input()
init_l = len(A)


def len_of_encoded(A):
    encoded_A = ""
    last_c = A[0]
    cnt = 0
    for char in A:
        if char == last_c:
            cnt += 1
        else:
            encoded_A += last_c + str(cnt)
            last_c = char
            cnt = 1
    encoded_A += last_c + str(cnt)
    return len(encoded_A)


min_l = init_l * 2
for _ in range(init_l):
    l = len_of_encoded(A)
    if l < min_l:
        min_l = l
    A = A[1:] + A[0]

print(min_l)
