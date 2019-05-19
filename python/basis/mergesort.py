
def merge_sort(lst):
    if len(lst) == 2:
        if lst[0] < lst[1]:
            return [lst[0], lst[1]]
        else:
            return [lst[1], lst[0]]
    elif len(lst) == 1:
        return [lst[0]]

    center = len(lst) // 2
    left = merge_sort(lst[:center])
    right = merge_sort(lst[center:])

    return merge(left, right)


def merge(left, right):
    result = []
    li = 0
    ri = 0
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            result.append(left[li])
            li += 1
        else:
            result.append(right[ri])
            ri += 1

    while li < len(left):
        result.append(left[li])
        li += 1

    while ri < len(right):
        result.append(right[ri])
        ri += 1

    return result


if __name__ == '__main__':
    lst = [3, 12, 43, 2, 0, 3, 2, 1]
    print(lst)
    print(merge_sort(lst))
