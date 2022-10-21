"""迭代器
	实现了方法__iter__的对象是可迭代的，而实现了方法__next__的对象是迭代器。
	调用方法__next__时（或者next()），迭代返回下一个值。如果迭代器没有可供返回的值，
	触发StopIteration异常。
	通过对可迭代对象调用内置函数，可获得一个迭代器
"""
class PowNumber(object):
	value=0
	"""docstring for PowNumber"""
	def __next__(self):
		self.value+=1
		if self.value>10:
			raise StopIteration
		return self.value * self.value

	def __iter__(self):
		return self

pow=PowNumber()
print(pow.__next__())
print(pow.__next__())
print(next(pow))
print(next(pow))
for i in pow:
	print(i)


"""生成器：generator
生成器是一种使用普通函数语法定义的迭代器。包含yield语句的函数都被称为生成器。
不使用return返回一个值，而是可以生成多个值，每次一个。
每次使用yield生成一个值后，函数都将冻结，即在此停止执行。
被重新唤醒后，函数将从停止的地方开始继续执行。

	1.推导式使用的符号
	2.函数+yield
		1.定义函数+添加关键字：yield
		2.调用函数得到的是一个生成器对象 g=func()
		3.结合next(g)
			只要通过yield则会将其后面值返回并暂停
			下一次调用next(g) --->从暂停位置开始执行
		4.如果函数有返回值，返回值的内容会作为，生成器里面的内容取完之后报错的信息：StepIteration 返回值的内容
函数：
   g.__next__()	同系统函数next(g)
   g.close()    关闭生成器
   g.send()	每次调用的时候向生成器传值,第一次必须send(None),以后就可以send(value)

"""
g=(x for x in range(3))
print(g) # <generator object <genexpr> at 0x0000023A16BF9EB0>
print(next(g))
print(next(g))
print(next(g))
print(next(g,5))

def func():
	sum=0
	for i in range(5):
		s=yield i
		print(s)
		sum+=(s+i)
		print('------>i',sum)

g=func()
print(g.__next__())

g.close()

g.send(None)
g.send(8)
######################################################
list1=[1,2,3,4,5]
g_pow=(x*x for x in list1)  
def pow_number():
	for x in list1:
		yield x*x
#######################################################
class IterRange(object):
	"""docstring for IterRange"""
	def __init__(self, start,end):
		
		self.start = start-1
		self.end=end
		
	def __next__(self):
		self.start+=1
		if self.start>=self.end:
			raise StopIteration
		return self.start
	def __iter__(self):
		return self

class GeneratorRange(object):
	"""docstring for GeneratorRange"""
	def __init__(self, start,end):
		
		self.start = start-1
		self.end=end
	def get_number(self):
		while True:
			if self.start>= self.end-1:
				break
			self.start+=1
			yield self.start


			
1、斐波那契数列
def func1(n):
	a,b=0,1
	for i in range(n):
		yield b
		a,b=b,a+b
	return "over"

g=func1(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__()) 	# StopIteration: over


2、递归函数
#递归函数：1.必须要有出口		2.不断向出口靠近
count=1
def func():
	global count
	if count==100:
		print('----->count',count)
	else:
		print('----->count',count)
		count+=1
		func()
func()

# 递归实现斐波那契数列
def fun(n):
	if n==1 or n==2:
		return 1
	else:
		return fun(n-1) + fun(n-2)


list_x=[]
for i in range(1,9):
	list_x.append(fun(i))
print(list_x)

