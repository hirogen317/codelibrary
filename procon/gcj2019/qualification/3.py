




def find_primes(n):
    if n<=2:
        return []
    sieve=[True]*(n+1)
    for x in range(3,int(n**0.5)+1,2):
        for y in range(3,(n//x)+1,2):
            sieve[(x*y)]=False
    return [2]+[i for i in range(3,n,2) if sieve[i]]


primes = find_primes(10000)


t = int(input())

for i in range(t):
    n, l = (int(x) for x in input().split(' '))
    nums = [int(x) for x in input().split(' ')]
    
print(n)
print(l)
