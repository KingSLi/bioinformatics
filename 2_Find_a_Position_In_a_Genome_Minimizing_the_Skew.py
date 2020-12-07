import numpy as np
genom = input()

skew = []
state = 0
skew.append(state)
for c in genom:
    if c == 'C':
        state -= 1
    elif c == 'G':
        state += 1
    skew.append(state)
skew = np.array(skew)
ans = np.where(skew == skew.min())
for x in ans[0]:
    print(x, end=" ")
