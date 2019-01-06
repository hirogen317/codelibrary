n  = int(input())

a = [int(x) for x in input().split()]

def get2(x):
    total = 0
    while x % 2 == 0:
        x = x // 2
        total += 1
    return total

total = 0
for x in a:

    total += get2(x)

print(total)
