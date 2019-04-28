
lst = ['a', 'b', 'c']
dic = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

for key, value in dic.items():
    print(key, ':', value)

for i, value in enumerate(lst):
    print(i, ':', value)

lst = [1, 4, 54, 1, 3, 45, 2, 4]

print(sorted(lst))
print(sorted(lst, reverse=True))


lst = [(2, 2), (1, 3), (2, 1), (1, 2), (1, 1), (2, 3)]
lst = sorted(lst, key=lambda item: item[1])
lst = sorted(lst, key=lambda item: item[0])

print()
for t in lst:
    print(t)
