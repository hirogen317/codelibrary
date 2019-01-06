n = int(input())

d = {}
last = None
result = True
for i in range(n):

    h = input()
    if h in d:
        result = False
    d[h] = 1
    if last:
        if last[-1] != h[0]:
            result = False
    last = h
if result:
    print("Yes")
else:
    print("No")
