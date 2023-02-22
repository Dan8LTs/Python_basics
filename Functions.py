def test_func():
    # pass - ничего не выполнять
    pass


test_func()


def test_func2(word):
    print(word, end="")
    print("!")


word = input()
test_func2(word)


def summ(n1, n2):
    return n1 + n2


res = summ(21, 5)
print(res)

subtract = lambda n1, n2: n1 - n2
print(subtract(13, 5))


def maximal(l):
    max = l[0]
    for el in l:
        if el > max:
            max = el
    print(max)


nums = [6, 3, 7, 8, 3, 9.0, 9]
maximal(nums)
