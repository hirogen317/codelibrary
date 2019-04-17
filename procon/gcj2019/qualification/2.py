
def find_another_route(pt, paths):
    

def decode_path(pt):
    current = (1,1)
    paths = [current]
    for t in pt:
        if t == 'E':
            current = (current[0], current[1] + 1)
        else:
            current = (current[0] + 1, current[1])
        paths.append(current)
    return paths


n = int(input())
for i in range(n):
    sz = int(input())
    pt = input()
    print(decode_path(pt))
