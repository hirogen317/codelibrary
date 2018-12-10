n = int(input())

primes = []
def prime():
    global primes
    primes = []
    for i in range(2,100):
        p = True
        for j in primes:
            if i % j == 0:
                p = False
                break
        if p:
            primes.append(i)

hash = {}
prime()

for i in range(1, n+1):
    k = i
    for j in primes:
        if k % j == 0:
            while k % j == 0:
                if j in hash:
                    hash[j] += 1
                else:
                    hash[j] = 1
                k = k // j
a = 0
b = 0
c = 0
d = 0
e = 0
for k, v in hash.items():
    if v >= 4:
        a += 1
    if v >= 2:
        b += 1
    if v >=14:
        c += 1
    if v >= 24:
        d += 1
    if v >= 74:
        e += 1

total = 0
if a<2 or b<3:
    print(0)
else:
    total = a*(a-1)*(b-2) // 2 + c *  (a-1) + d * (b-1) + e
    print(total)
