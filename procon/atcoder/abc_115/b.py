n = int(input())

total = 0
maxp = 0
for i in range(n):
    p = int(input())
    if p > maxp:
        maxp = p
    total += p

total -= maxp // 2

print(total)
