#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from multiprocessing import Process

__author__ = 'zbcn8'

def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target=run_proc, args=('test',));
	print('Child process will start.')
	p.start()
	# 等待子进程结束
	p.join()
	print('Child process end.')