#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

__author__ = 'zbcn8'

# 一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
def generate_code(code_len=4):
	"""
	生成指定长度的验证码

	:param code_len: 验证码的长度(默认4个字符)

	:return: 由大小写英文字母和数字构成的随机验证码
	"""
	all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	last_pos = len(all_chars) - 1
	code = ''
	for _ in range(code_len):
		index = random.randint(0, last_pos)
		code += all_chars[index]
	return code

# 一个函数返回给定文件名的后缀名。
def get_suffix(filename, has_dot=False):
	"""
	获取文件名的后缀名

	:param filename: 文件名
	:param has_dot: 返回的后缀名是否需要带点
	:return: 文件的后缀名
	"""
	pos = filename.rfind('.')
	if 0 < pos < len(filename) - 1:
		index = pos if has_dot else pos + 1
		return filename[index:]
	else:
		return ''

# 一个函数返回传入的列表中最大和第二大的元素的值
def max2(x):
	m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
	for index in range(2, len(x)):
		if x[index] > m1:
			m2 = m1
			m1 = x[index]
		elif x[index] > m2:
			m2 = x[index]
	return m1, m2

# 计算指定的年月日是这一年的第几天。
def is_leap_year(year):
	"""
	判断指定的年份是不是闰年

	:param year: 年份
	:return: 闰年返回True平年返回False
	"""
	return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
	"""
	计算传入的日期是这一年的第几天

	:param year: 年
	:param month: 月
	:param date: 日
	:return: 第几天
	"""
	days_of_month = [
		[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
		[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	][is_leap_year(year)]
	total = 0
	for index in range(month - 1):
		total += days_of_month[index]
	return total + date


if __name__ == '__main__':
    print(generate_code())

    print('文件名后缀：%s' % get_suffix('aaa.txt'))