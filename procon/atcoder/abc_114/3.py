s = input()

n = int(s)

a = []
total = 0


def is_753(a):
    return set(a) == set([7,5,3])

def get_int(a):
    result = 0
    for i in range(len(a)):
        result = result * 10 + a[len(a) - i - 1]
    return result

def dfs(a, k):
    global total
    if is_753(a):
        total += 1
    for next_x in [3,5,7]:
        a.append(next_x)
        if get_int(a) <= k:
            dfs(a, k)
            a.pop()
        else:
            a.pop()
            break

dfs(a, n)
print(total)
