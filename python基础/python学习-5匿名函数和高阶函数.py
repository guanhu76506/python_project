1、匿名函数
# 函数体非常简单、使用次数较少
# 定义格式：lambda 参数:返回值
f=lambda n:n+1
print(f)  #<function <lambda> at 0x000001517E1771F0>
print(f(5)) # 6


2、高阶函数
"""
高阶函数：把函数当成参数进行传递的函数
	1.sorted(iterable,key,reverse)
		通过key指定排序规则
	2.map(function,iterable)  返回map对象
		给一个可迭代的对象，通过function的作用，将其转换为一个新的对象
	3.filter(function,iterable) 返回filter对象
		If function is None, return the items that are true.
		function的返回值必须是bool类型
	4.reduce(function,iterable)  返回value
	5.partial() 偏函数
		通过一个函数的部分参数预先绑定为某些值，从而得到一个新的具有较少可变参数的函数
	6.wraps() 
		消除装饰器带来的一些副作用
"""
def fun(f): #函数名作为参数
	r=f(5)
	r+=10
	return r

result=fun(lambda x:x*2)  #result的值为 20

#sorted函数学习
def func(x):
	return x[1]
list1=[("zhangsan",3),("zhaoliu",6),("tianqi",7),("lisi",4),("wangwu",5)]
list2=sorted(list1,key=(lambda x:x[1]),reverse=True) 
#输出结果：[('tianqi', 7), ('zhaoliu', 6), ('wangwu', 5), ('lisi', 4), ('zhangsan', 3)]
list3=sorted(list1,key=func,reverse=False)
#输出结果：[('zhangsan', 3), ('lisi', 4), ('wangwu', 5), ('zhaoliu', 6), ('tianqi', 7)]
dict1 = {"zhangsan": 3, "zhaoliu": 6, "tianqi": 7, "lisi": 4, "wangwu": 5}
result = sorted(dict1.items(), key=lambda x: x[1])  # 通过key这个函数指定规则
dict1=dict(result)
print(dict1)

#map函数学习
list4 = [1, 2, 3, 4, 5]
map1 = map(lambda x: x ** 2, list4)
print(map1)			# <map object at 0x0000029FA5051190>
print(list(map1))  	# [1, 4, 9, 16, 25]

#filter函数学习
f1 = filter(lambda x: x % 2 == 0, list4)
print(f1)      	# <filter object at 0x000001B6934E1190>
print(list(f1)) # [2, 4]
list5=['hello',1,2,3,"50","h100",'yes'] #过滤元素，得到数字或者字符串内容为数字
f1 = filter(lambda x: str(x).isdigit(), list5)  #方法1
f2 = filter(lambda x: isinstance(x, int) or x.isdigit(), list5) #方法2
list1=[("zhangsan",3),("zhaoliu",6),("tianqi",7),("lisi",4),("wangwu",5)]
f3=filter(lambda x:x[1]>5,list1)
print(list(f3))

#reduce函数学习
from functools import reduce
list6=[1,2,3,4]
value=reduce(lambda x,y:x+y,list6,2) #累加 结果为12  
list7 = ['a','b','c','d']
value = reduce(lambda x, y: x + y, list7)    #abcd
 """
    reduce(function, sequence[, initial]) -> value
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
"""
jc=reduce(lambda x,y:x*y,range(1,6)) #阶乘  结果为120

#partial() 偏函数学习
def add(a, b):
    return a + b
add1 = partial(add, 3)
print(add1(5))
int1 = partial(int, base=8)
print(int1('0011'))


#wraps函数学习
"""
Decorator factory to apply update_wrapper() to a wrapper function
   Returns a decorator that invokes update_wrapper() with the decorated
   function as the wrapper argument and the arguments to wraps() as the
   remaining arguments. Default arguments are as for update_wrapper().
   This is a convenience function to simplify applying partial() to
   update_wrapper().
"""
def decorator1(func):
	@wraps(func)
	def wrapper1(*args,**kwargs):
		func(*args,**kwargs)
		print('铺地板')
		print('刷漆')
	return wrapper1


def decorator2(func):
	def wrapper2(*args,**kwargs):
		func(*args,**kwargs)
		print('买衣柜')
		print('买沙发')
		print('买电视、冰箱')
	return wrapper2

@decorator2		# 第二层装饰器
@decorator1  	# 第一层装饰器
def hourse():
	print("---->毛坯房")

hourse()

print(hourse.__name__) #wrapper2
print(hourse.__doc__)  #None

################################################################

def log(name=None):
	def decorator(func):
		@wraps(func)
		def wrapper(*args,**kwargs):
			print('{}start...'.format(name))
			print('wrapper name {}'.format(func.__name__))
			print("@wrapper doc {}".format(func.__doc__))
			rest=func(*args,**kwargs)
			print('{}end...'.format(name))
			return rest
		return wrapper
	return decorator
@log('h')
def hello():
	print('hello')

print(hello.__doc__)
print(hello.__name__)
