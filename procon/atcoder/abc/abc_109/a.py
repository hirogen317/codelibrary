a, b = (int(x) for x in input().split())

if a * b % 2 == 0:
    print("No")
else:
    print("Yes")
