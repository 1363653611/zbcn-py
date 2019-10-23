#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from inspect import getgeneratorstate

__author__ = 'zbcn8'


def jump_range(N):
	index = 0
	while index < N:
		# 通过send()发送的信息将赋值给jump
		jump = yield index
		if jump is None:
			jump = 1
		index += jump


# 协程
def test_jump_range():
	itr = jump_range(5)
	print(next(itr))
	# 生成器暂停的时候向其发送一点东西
	print(itr.send(2))
	print(next(itr))
	print(itr.send(-1))


def mygen(n):
	now = 0
	while now < n:
		yield now
		now +=1


# 生成器的状态测试
def test_mygen():
	gen = mygen(2)
	print(getgeneratorstate(gen))
	print(next(gen))
	print(getgeneratorstate(gen))
	print(next(gen))
	gen.close()  # 手动关闭/结束生成器
	print(getgeneratorstate(gen))


"""
1. 可迭代对象:可迭代对象，是其内部实现了，__iter__ 这个魔术方法。
2. 迭代器:迭代器，是其内部实现了，__next__ 这个魔术方法。(Python3.x)
3. 生成器:在迭代器的基础上（可以用for循环，可以使用next()），再实现了yield
	生成器的生命周期:
	GEN_CREATED # 等待开始执行
	GEN_RUNNING # 解释器正在执行（只有在多线程应用中才能看到这个状态）
	GEN_SUSPENDED # 在yield表达式处暂停
	GEN_CLOSED # 执行结束
	
4. 协程:协程是为非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停或开始执行程序。
"""
if __name__ == '__main__':
	# test_jump_range()
	test_mygen()
