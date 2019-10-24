#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from types import MethodType

__author__ = 'zbcn8'

class student(object):
	# 对象构造:name 和 score 是必传值
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	# __ 代表改属性为私有属性,不能通过 student.__score 访问
	def getScore(self):
		return self.__score


class Animal(object):
	def run(self):
		print('animal running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')

def setName(self, name):
	self.__name = name

def getName(self):
	return self.__name


if __name__ == '__main__':
    student = student("zhansan",90)
    print(student.getScore())
    # 给示例添加方法
    student.setName = MethodType(setName, student)
    student.getName = MethodType(getName, student)
    student.setName("lsi")
    print(student.getName())
    dog = Dog()
    print(dog.run())
    print(isinstance(dog, Animal))
    print(isinstance(dog, Dog))