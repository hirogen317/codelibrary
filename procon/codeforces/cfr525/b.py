t, k = (int(i) for i in input().split())
a = list(set([int(i) for i in input().split()]))
a.sort()

total = 0
i = 0

for i in range(k):
    if a[-1] - total == 0:
        print(0)
    else:
        print(a[i] - total)
        total += a[i] - total
