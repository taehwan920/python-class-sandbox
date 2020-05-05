import random

a = list(random.sample(range(100), 12))


def merge(left, right):
    merged = []
    left_point, right_point = 0, 0

    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged


def split(data_li):
    if len(data_li) == 1:
        return data_li
    medium = int(len(data_li) / 2)
    left = split(data_li[:medium])
    right = split(data_li[medium:])
    print(left, right)
    return merge(left, right)


split(a)
