#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host='localhost', prot=3306, user='root', password='123456', db='python', charset='utf8')
db.cursur()


if __name__ == '__main__':
    print('test')
