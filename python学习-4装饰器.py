1、闭包概念
	1.一个函数定义了另外一个函数
	2.内部函数引用了外部函数的变量
	3.返回的是内部函数名
def outer_func(n):
	a=10
	def inner_func()
		r=a+n
		print("r的值：",r)
	print(locals())
	return inner_func # 返回内部函数名

result=outer_func(1)  #result就是一个内部函数(inner_func())的地址
print(result)
result() #调用内部函数

2、函数作为参数使用
def A():
	print("hello world")
def func2(f): # f 为 A的地址
	print("----->")
	f()
	print("----->over")
func2(A)


def func3(f):
	print('---->start:',f)
	def inner_func():
		print("-------->inner_func")
		f()
	print('---->end:',f)
	return inner_func
result=func3(A)
print(result)
result()


3、装饰器功能
	1、引入日志
	2、函数执行时间统计
	3、执行函数的预备处理
	4、执行函数后的清理功能
	5、权限校验场景
	6、缓存(redis)
#1.定义函数，闭包的原则+函数作为参数   装饰器函数
def func(f):
	print("----------->1")
	def wrapper():
		print("装饰前......验证是否登录")
		f()
		print("装饰后......")
	print("------------>2")
	return wrapper

#2.功能函数
#①调用func函数 ②执行函数体中的内容 ③加载内部函数 
#④返回内部函数wrapper ⑤buy_ticket接收了func的返回值，buy_ticket=wrapper
@func 
def buy_ticket():
	print("我可以买票了")

#3.买票
buy_ticket()

代码运行后的结果：
----------->1
------------>2
装饰前......验证是否登录
我可以买票了
装饰后......

print(buy_ticket) #<function func.<locals>.wrapper at 0x000001F05AB0BD30>


4、装饰有返回值的函数
"""
要装饰的函数有返回值，装饰器的内层函数也要有返回值，
从而保证装饰后的函数与原函数保持一致性
"""
flag=False

#定义一个装饰器函数
def decorator(func):  #如果func(本例指向isloign函数)有返回值则内层函数也要有返回值
	def wrapper(*args,**kwargs):
		print('进行用户的登录验证')
		r=func(*args,**kwargs)
		if r:
			return 'success'
		else:
			return 'fail'
	return wrapper

def login():
	global flag 	
	username=input("输入用户名")
	password=input("输入密码")
	if username='admin' and password='123':
		flag=True
@decorator
def isloign():
	if flag:
		return True
	else:
		return False
login()

r=isloign()
print(r)

5、使用装饰器进行用户的登录验证
isloign=False

#定义装饰器函数，进行登录验证
def login_required(func):
	def wrapper(*args,**kwargs):
		global isloign
		if isloign:
			func()
		else:
			print('----用户没有登录，请登录')
			f=login()
			if f:
				func()
	return wrapper

def login():
	global isloign 
	username=input("输入用户名")
	password=input("输入密码")
	if username=='admin' and password=='123':
		isloign=True
		return isloign
	return isloign

@login_required
def buy_ticket():
	ticket={"中华影城":["哪吒",['11:30 1号厅','12:30 3号厅','14:30 5号厅']]}
	for key,value in ticket.items():
		print('影城',key)
		print('播放的电影是：',value[0])
		print('播放时间是：')
		for i in value[1]:
			print('--->',i)
login()

buy_ticket()

6、装饰器带有参数
"""
	三层函数实现的
	def 装饰器名(装饰器参数):
		def second(函数参数):
			def third(*args,**kwargs):
				...
				...
			return third
		return second
"""
def decorator(n):
	print('-------->1')
	def decorator1(func):
		print('-------->2')
		def wrapper(*args,**kwargs):
			print('-----start')
			func(*args,**kwargs)
			print('-----end')
		print('-------->3')
		return wrapper
	print('-------->4')
	return decorator1

@decorator(10)
def show():
	print('----->调用show函数')

show()
输出结果：
-------->1
-------->4
-------->2
-------->3
-----start
----->调用show函数
-----end
##########################################################################
def log(name=None):
	def decorator(func):
		def wrapper(*args,**kwargs):
			print('{}start...'.format(name))
			print(args)
			print(kwargs)
			rest=func(*args,**kwargs)
			print('{}end...'.format(name))
			return rest
		return wrapper
	return decorator
@log('h')
def hello():
	print('hello')
@log('a')
def add(a,b):
	return a+b

hello()
#输出结果:
hstart...
()
{}
hello
hend...

res = add(1, 2)
print(res)
#输出结果:
astart...
(1, 2)
{}
aend...
3
7、多层装饰器
"""
谁离原函数最近先执行哪个装饰器，将第一层装饰器的返回结果传给第二层装饰器。
最后：原函数得到的地址是第二层函数的返回值wrapper
"""
#例子1
def decorator1(func):
	print(func.__name__) 	# hourse
	def wrapper1(*args,**kwargs):
		func(*args,**kwargs)
		print('铺地板')
		print('刷漆')
	return wrapper1


def decorator2(func):
	print(func.__name__) 	# wrapper1
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
输出结果：
---->毛坯房
铺地板
刷漆
买衣柜
买沙发
买电视、冰箱

#例子2：
def log(func):
    def wrapper1():
        print('start...')
        func()
        print('end...')
    return wrapper1

def login(f):
    def wrapper2():
        print('开始。。。')
        f()
        print('结束。。。')
    return wrapper2

@log    #第二层
@login  #第一层
def hello():
    print('hello')

hello()
#输出结果：
start...
开始。。。
hello
结束。。。
end...


def decorator(func):
	count=0
	def wrapper():
		nonlocal count
		func()
		count+=1
		print('第{}次调用{}函数'.format(count,func.__name__))
	return wrapper

@decorator
def show():
	print('这里正在调用show函数')



def decorator(func):
	
	def wrapper():
		
		func()
		count+=1
		print('调用{}函数'.format(func.__name__))
	return wrapper

@decorator
def show():
	print('这里正在调用show函数')
	
@decorator
def test(n):
	print('------>',n)
