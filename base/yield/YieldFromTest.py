#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zbcn8'

# 字符串
astr = 'ABC'

# 列表
alist = [1, 2, 3]

# 字典
adict = {"name":"wangbm", "age":18}

# 生成器
agen = (i for i in range(4, 8))
agen_2 = (i for i in range(4, 10))


# 使用 yield
def gen(*args):
	for item in args:
		for i in item:
			yield i


# 拼接可迭代对象
def testYield():
	new_list = gen(astr, alist, adict, agen)
	print(list(new_list))


# 使用yield from
def gen_2(*args):
	for item in args:
		# yield from后面加上可迭代对象，他可以把可迭代对象里的每个元素一个一个的yield出来
		yield from item

# 拼接可迭代对象
def test_yield_from():
	new_list2 = (astr, alist, adict, agen_2)
	print(list(new_list2))



"""
1、调用方：调用委派生成器的客户端（调用方）代码
2、委托生成器：包含yield from表达式的生成器函数
3、子生成器：yield from后面加的生成器函数
"""


# 子生成器
def sun_gen():
	total = 0
	count = 0
	average = 0
	while True:
		new_num = yield average
		count += 1
		total += new_num
		average = total/count


# 委托生成器
def proxy_gen():
	while True:
		yield from sun_gen()


# 调用方
def main():
	#委托生成器
	calc_average = proxy_gen()
	first = next(calc_average)            # 预激下生成器
	print(first)
	print(calc_average.send(10))  # 打印：10.0
	print(calc_average.send(20))  # 打印：15.0
	print(calc_average.send(30))  # 打印：20.0


if __name__ == '__main__':
    testYield()
    test_yield_from()
    main()


