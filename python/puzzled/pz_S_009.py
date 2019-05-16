
def sort(seq, pt):
    result = []
    for i in pt:
        result.append(seq[i-1])

    return result


def search(seq, pt):
    if len(pt) == 0:
        return seq

    results = []
    for i in range(len(pt)):
        np = pt[:]
        np.pop(i)
        r = search(sort(seq, pt[i]), np)
        results.append(r)

        r = search(seq, np)
        results.append(r)

    return min(results)


n = 3
n = int(n)

s = '3 1 2'.split()
s = [int(c) for c in s]

m = 2
m = int(m)

pattern = [
    [1, 3, 2],
    [2, 3, 1]
]

result = search(s, pattern)
print(result)
