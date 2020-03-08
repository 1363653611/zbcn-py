from types import MethodType
class Student(object):
	# 控制对象可以添加的属性。在__sorts__ 不存在的属性不允许添加
	slots__ = ("name", "age", "score")
	pass

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, (int, float)):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		else:
			self._score = value





def set_age(self, age):
	self.age = age

if __name__ == '__main__':
    # 判断类型
    # t = type(123)
	# dir 命令是获得对象的所有属性和方法
    #print(dir("object"))
    #print(type(abs))
	s = Student()
    # 给实例添加属性
	s.set_age = MethodType(set_age, s)
	s.set_age(25)
	print(s.age)
	s.score = 100
	print(s.score)

