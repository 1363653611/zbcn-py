#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zbcn8'

# 使用变量保存数据并进行算术运算
def var():
	a = 321
	b = 123
	print(a + b)
	print(a - b)
	print(a * b)
	print(a / b)
	print(a // b)
	print(a % b)
	print(a ** b)


# 使用type()检查变量的类型
def check_type():
	a = 100
	b = 12.345
	c = 1 + 5j
	d = 'hello, world'
	e = True
	print(type(a)) # <class 'int'>
	print(type(b)) # <class 'float'>
	print(type(c)) # <class 'complex'>
	print(type(d)) # <class 'str'>
	print(type(e)) # <class 'bool'>


"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串
"""
def input_test():
	a = int(input('a = '))
	b = int(input('b = '))
	print('%d + %d = %d' % (a, b, a + b))
	print('%d - %d = %d' % (a, b, a - b))
	print('%d * %d = %d' % (a, b, a * b))
	print('%d / %d = %f' % (a, b, a / b))
	print('%d // %d = %d' % (a, b, a // b))
	print('%d %% %d = %d' % (a, b, a % b))
	print('%d ** %d = %d' % (a, b, a ** b))


def str():
	s1 = 'hello, world!'
	s2 = "hello, world!"
	# 以三个双引号或单引号开头的字符串可以折行
	s3 = """
	hello, 
	world!
	"""
	print(s1, s2, s3, end='')

if __name__ == '__main__':
	# var()
	# check_type()
	input_test()
	# str()