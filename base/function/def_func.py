import math


# 定义一个返回整数的方法
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand error")
    if x > 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    # 余玄
    nx = x + step * math.cos(angle)
    """ 正玄"""
    ny = y + step * math.sin(angle)
    return nx, ny


if __name__ == '__main__':
    n = my_abs(-20)
    print(n)
    x, y = move(100, 100, 60, math.pi / 6)
    print(x, y)
    # TypeError: bad operand type:
    my_abs('123')
