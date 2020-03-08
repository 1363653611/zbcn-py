# -*- coding: utf-8 -*-
__author__ = 'zbcn8'

import requests

def testUrl():
	r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
	print(r.url)
	print(r.encoding)

if __name__ == '__main__':
    r = requests.get("http://www.baidu.com")
    print(r.status_code)
    print(r.text)
    testUrl()