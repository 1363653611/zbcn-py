import functools


def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print("call %s()" % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print("测试时间。。。")

if __name__ == '__main__':
    now()