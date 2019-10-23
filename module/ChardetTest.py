# -*- coding: utf-8 -*-
import chardet

__author__ = 'zbcn8'


def checkCharSet(str):
	ty = chardet.detect(str)
	print(ty)

"""
检测输入字符串的字符集
"""
if __name__ == '__main__':
	char = chardet.detect(b'Hello, world!')
	print(char)
	data = '离离原上草，一岁一枯荣'.encode('gbk')
	checkCharSet(data)