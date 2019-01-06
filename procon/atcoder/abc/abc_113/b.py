n  = int(input())
t, a = (int(x) for x in input().split())
h = [int(x) for x in input().split()]


total = None
result = 0

for i, x in enumerate(h):
    temp =   t - 0.006* x
    if total is None or abs(a - temp) < total:
        total = abs(a - temp)
        result = i + 1
print(result)
