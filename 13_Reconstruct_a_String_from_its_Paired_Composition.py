from collections import defaultdict

with open("input.txt", "r") as f:
    k, d = map(int, f.readline().split())
    lines = [line.strip() for line in f.readlines()]

g = defaultdict(list)
balance = defaultdict(int)
for line in lines:
    upper, down = line.split('|')
    node1 = (upper[:-1], down[:-1])
    node2 = (upper[1:], down[1:])
    g[node1].append(node2)
    balance[node1] -= 1
    balance[node2] += 1

start = None
for key, v in balance.items():
    if v < 0:
        start = key
        break

stack = [start]
ans = []
while len(stack) > 0:
    v = stack[-1]
    if v not in g or len(g[v]) == 0:
        ans.append(v)
        stack.pop(-1)
    else:
        u = g[v][-1]
        g[v].pop(-1)
        stack.append(u)

ans.reverse()


a = []
b = []
for up, down in ans:
    if len(a) == 0:
        for i in range(len(up)):
            a.append(up[i])
            b.append(down[i])
    else:
        a.append(up[-1])
        b.append(down[-1])

print("".join(a + b[-(d + k):]))
