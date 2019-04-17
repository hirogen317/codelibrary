
def rid4(x):
    k = x
    r_array = []
    r1 = 0
    while k > 0:
        y = k % 10
        if y == 4:
            r_array.append(2)
        else:
            r_array.append(y)
        k = k // 10
    r_array.reverse()
    for r in r_array:
        r1 = r1 * 10 + r
    return r1, x - r1


n = int(input())
for i in range(n):
    x = int(input())
    r1, r2 = rid4(x)
    print("Case #{}: {} {}".format(i+1, r1, r2))
