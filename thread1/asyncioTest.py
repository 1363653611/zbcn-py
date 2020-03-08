#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import threading

__author__ = 'zbcn8'


@asyncio.coroutine
def hello():
	print('Hello world! (%s)' % threading.currentThread())
	yield from asyncio.sleep(1)
	print('Hello again! (%s)' % threading.currentThread())


@asyncio.coroutine
def hi():
	print('how are you! (%s)' % threading.currentThread())
	yield from asyncio.sleep(0.5)
	print('how are you! (%s)' % threading.currentThread())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = [hello(), hi()]
    loop.run_until_complete(asyncio.wait(task))