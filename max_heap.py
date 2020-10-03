b = []


def heappush(item):
    b.append(item)
    b = [None] + b
    idx = len(b) - 1
    while idx > 1:
        parent = idx // 2
        print(parent, idx, b[parent], b[idx])
        if b[idx] > b[parent]:
            b[parent], b[idx] = b[idx], b[parent]
            idx = parent
        else:
            break
    print(b)
    b = list(b[1:])


def heappop(arr):
    arr = [None] + arr
    idx = 1
    last = len(arr) - 1
    popped = arr[idx]
    while idx < last:
        left = 2 * idx
        right = left + 1
        if right > last:
            arr[idx] = arr[left]
            idx = left
        if left < right:
            arr[idx] = arr[right]
            idx = right
        else:
            arr[idx] = arr[left]
            idx = left

    return popped


def heapify(li):
    new = []
    for i in range(len(li)):
        heappush(new, li[i])
    return new


a = [2, 4, 6, 8, 10]


for num in a:
    heappush(num)
