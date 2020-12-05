perm = list(map(int, input()[1:-1].split()))
perm = [0] + perm + [len(perm) + 1]
breakpoints_cnt = 0
for i in range(len(perm) - 1):
    if perm[i] * perm[i + 1] >= 0:
        breakpoints_cnt += perm[i] + 1 != perm[i + 1]
    else:
        breakpoints_cnt += 1
print(breakpoints_cnt)
