n,m = (int(x) for x in input().split())

p = [0] * m
y = [0] * m
d = {}

for i in range(m):
    p[i] , y[i] = (int(x) for x in input().split())
    if p[i] in d:
        d[p[i]].append(y[i])
    else:
        d[p[i]] = [y[i]]

sort_dict = {}

for k in d.keys():
    v = d[k]
    for i, num in enumerate(sorted(v)):
        
