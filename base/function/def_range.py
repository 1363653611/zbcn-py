from functools import reduce


def text():
    print(list(range(0, 11)))


def testMap():
    print(list(map(str, [1, 2, 4, 5, 6, 7, 8])))


def testReduce():
    result = reduce(fn, [1, 2, 4, 5, 6, 7, 8])
    print(result)
    pass


def fn(x, y):
    if not (isinstance(x, int) or isinstance(y, int)):
        raise TypeError("error param type")
    return x * 10 + y


# 返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    # 返回函数
    return sum


if __name__ == '__main__':
    # text()
    # testMap()
    testReduce()
    _sum = lazy_sum(1, 3, 5, 6)
    print(_sum)
    print(_sum())
