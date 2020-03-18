def fibo(num):
    if num <= 2:
        return 1
    else:
        return fibo(num-1) + fibo(num-2)


def to_where(num):
    for i in range(1, num+1):
        print(fibo(i))


to_where(10)
