import random


def quick_sort(data_li):
    if len(data_li) <= 1:
        return data_li
    pivot = data_li[0]

    left = []
    right = []

    for i in range(1, len(data_li)):
        if data_li[i] < pivot:
            left.append(data_li[i])
        else:
            right.append(data_li[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


a = list(random.sample(range(100), 50))

print(quick_sort(a))
