from fractions import gcd


def gcd_array(a):
    gg = gcd(a[0],a[1])

    for i in range(2, len(a)):
        gg = gcd(gg, a[i])
    return gg


n, x = (int(i) for i in input().split())

b = [abs(int(k) - x) for k in input().split()]

if len(b) == 1:
    print(b[0])
else:
    print(gcd_array(b))
