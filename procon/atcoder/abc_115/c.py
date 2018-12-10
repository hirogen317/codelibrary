n, k = (int(x) for x in input().split())

h = [0] * n
for i in range(n):
    h[i] = int(input())

h.sort()

total = None
for i in range(n - k + 1):
    diff = h[i+k-1] - h[i]
    if total is None or total > diff:
        total = diff

print(total)
