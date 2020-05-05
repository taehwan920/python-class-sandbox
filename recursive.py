# 재귀를 활용해 1 ~ n의 곱이 출력되도록 하라.


def multiple(num):
    if num == 1:
        return 1
    else:
        print(num)
        return num * multiple(num - 1)


print(multiple(10))


def sum_li(li):
    if len(li) <= 1:
        return li[0]
    else:
        return li[0] + sum_li(li[1:])


def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False
