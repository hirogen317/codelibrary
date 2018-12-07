import math
s = list(input())

total = 753
for i in range(len(s) - 2):
    a = int(s[i]) * 100 + int(s[i+1]) * 10 + int(s[i+2])
    if total >= abs(a - 753):
        total = abs(a - 753)

print(total)
