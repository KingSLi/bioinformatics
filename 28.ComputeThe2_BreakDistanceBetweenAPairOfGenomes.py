from collections import defaultdict
import sys


def read_genom():
    return [list(map(int, part.strip(' ()').split())) for part in input().split(')(')]


def add_part_to_graph(part, g):
    m = len(part)
    for i in range(m):
        from_, to = part[i], part[(i + 1) % m]
        to *= -1
        g[from_].append(to)
        g[to].append(from_)


def dfs(g, used, i):
    used[i] = 1
    for to in g[i]:
        if to not in used:
            dfs(g, used, to)


sys.setrecursionlimit(10000000)
g1 = read_genom()
g2 = read_genom()

n = max(
    abs(max([max(x) for x in g1])),
    abs(min([min(x) for x in g1]))
)

g = defaultdict(list)
for part in g1:
    add_part_to_graph(part, g)
for part in g2:
    add_part_to_graph(part, g)
used = {}
count = 0
for v in g:
    if v not in used:
        dfs(g, used, v)
        count += 1

print(n - count)
