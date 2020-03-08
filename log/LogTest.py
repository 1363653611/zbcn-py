# -*- coding: utf-8 -*-
import time

__author__ = 'zbcn8'
import logging
from log import ZbcnLog #导入自定义的logging配置
logger = logging.getLogger(__file__)  # 生成logger实例

def demo():
	logger.debug("start range... time:{}".format(time.time()))
	logger.info("中文测试开始。。。")
	for i in range(10):
		logger.debug("i:{}".format(i))
		time.sleep(2)
	else:
		logger.error("over range... time:{}".format(time.time()))
	logger.info("中文测试结束。。。")

if __name__ == "__main__":
	demo()