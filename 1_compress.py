
def pleaseConform(seq):
    if len(seq) == 0:
        return

    seq = seq + ['H']
    start = 0
    while seq[start] == 'H':
        start += 1

    for i in range(start+1, len(seq)):
        if seq[i] != seq[i-1]:
            if seq[i] != seq[start] and seq[i] != 'H':
                s = i
            elif s != -1:
                if s == i-1:
                    print(f'Person in position {s}, please flip your cap.')
                else:
                    print(f'Person in position {s} through {i-1}, please flip your caps.')
                s = -1

cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
pleaseConform(cap1)

print()

cap2 = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']
pleaseConform(cap2)
