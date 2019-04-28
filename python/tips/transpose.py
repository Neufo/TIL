
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

transposed = [ [row[i] for row in matrix] for i in range(3)]
for row in transposed:
    print(row)

print()

transposed = list(zip(*matrix))
for row in transposed:
    print(row)

