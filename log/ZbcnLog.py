# -*- coding: utf-8 -*-
__author__ = 'zbcn8'
"""
logging 配置文件
"""
import os
import logging.config
# 定义三种日志输出格式
standard_format = '[%(asctime) -s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束

logfile_dir = os.path.dirname(os.path.abspath(__file__))  # log文件的目录

logfile_name = 'zbcn.log'  # log文件名
err_file_name = 'error.log'

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
	os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

err_file_path = os.path.join(logfile_dir, err_file_name)

# log配置字典
LOGGING_DIC = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'standard': {
			'format': standard_format,
			'datefmt': '%Y-%m-%d %H:%M:%S',
		},
		'simple': {
			'format': simple_format
		},
		'id_simple': {
			'format': id_simple_format
		}
	},
	'filters': {},
	'handlers': {
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',  # 打印到屏幕
			'formatter': 'simple'
		},
		'default': {
			'level': 'DEBUG',
			'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
			'filename': logfile_path,  # 日志文件
			'maxBytes': 1024*1024*5,  # 日志大小 5M
			'backupCount': 5,
			'formatter': 'standard',
			'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
		},
		'error': {
			'level': 'ERROR',
			'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
			'filename': err_file_path,  # 日志文件
			'maxBytes': 1024*1024*5,  # 日志大小 5M
			'backupCount': 5,
			'formatter': 'standard',
			'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
		},
	},
	'loggers': {
		'': {
			'handlers': ['default', 'console', 'error'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
			'level': 'DEBUG',
			'propagate': True,  # 向上（更高level的logger）传递
		},
	},
}
logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的配置
logger = logging.getLogger(__name__)  # 生成一个log实例
logger.info('It works!')  # 记录该文件的运行状态

