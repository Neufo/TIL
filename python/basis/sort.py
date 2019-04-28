import random

def bubble(lst):
    result = lst[:]
    for i in range(0, len(lst)-1):
        for j in range(len(lst)-1, i, -1):
            if result[j-1] > result[j]:
                result[j-1], result[j] = result[j], result[j-1]
    return result

def insertion(lst):
    result = lst[:]
    for i in range(len(lst)-1):
        pos = i
        for j in range(i+1, len(lst)):
            if result[j] < result[pos]:
                pos = j
        result[i], result[pos] = result[pos], result[i]
    return result


def print_result(lst, sort_method):
    print('method:', str(sort_method))
    print('before:', lst)
    print('after:', sort_method(lst))
    print()


if __name__ == '__main__':
    random.seed(0)
    lst = [random.randint(0,100) for _ in range(10)]

    print_result(lst, bubble)
    print_result(lst, insertion)

