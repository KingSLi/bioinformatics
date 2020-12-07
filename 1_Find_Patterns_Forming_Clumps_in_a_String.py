from collections import defaultdict


genom = input()
k, l, t = map(int, input().split())
ans = set()
for s in range(len(genom) - l + 1):
    g = genom[s: s + l]
    st = defaultdict(int)
    for i in range(l + 1 - k):
        st[g[i: i + k]] += 1
    for key, v in st.items():
        if v >= t:
            ans.add(key)
print(' '.join(ans))
