import re

def encode(s):
    if len(s) == 0:
        return ''
    result = []
    start = 0
    run = s[0]
    s = s + '\0'
    for i in range(1, len(s)):
        if s[i] != run:
            result.append(f'{i-start}{run}')
            run = s[i]
            start = i
    
    return ''.join(result)

def decode(s):
    result = []
    for p in re.findall(r'[1-9]+\D+', s):
        count = int(p[:len(p)-1])
        char = p[len(p)-1]
        result.append(char*count)
    return ''.join(result)

s1 = 'BWWWWWBWWWW'
print(s1)
e1 = encode(s1)
print(e1)
d1 = decode(e1)
print(d1)

print()
s2 = 'wwwwb'
print(s2)
e2 = encode(s2)
print(e2)
d2 = decode(e2)
print(d2)


