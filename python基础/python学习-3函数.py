1、函数传参的使用技巧
import random
#生成验证码
def generator_code(length) 
	code=""
	s="1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
	for i in range(length):
		ran=random.choice(s)
		code+=ran
	print("本次验证码是：",code)
def func(name, friends):
    print("{}的朋友如下：".format(name))
    if isinstance(friends, Iterable):
        for friend in friends:
            print(friend)
    else:
        print(friends)

def add_friend(friends):
    name = input("输入朋友的名字")
    if isinstance(friends, list):
        friends.append(name)
name = '钢铁侠'
friends = ['a', 'b', 'c', 'd']
func(name=name, friends=friends)
add_friend(friends)
print(friends)

#函数的参数：
	不可变的参数给的是值，int,float,str,tuple
	可变的参数给的是地址  list,dict,set
#例子1：
number=10
list_x=[]
def change_number(n,list1):
    n+=1
    print("修改后的n值是：",n)
    list1.append(6)
    list1.append(7)
change_number(number,list_x) #11
print(number)  # 10
print(list_x)  # [6,7]

#例子2：
name='jack'
def change_name(name):	
    name=name[::-1] 
    print("新的名字",name)
change_name(name) #kcaj
print(name) #jack
1.5.1、为参数设置默认值 
在定义函数的时候对某个参数设置一个固定的值，定义默认值的时候需要放在参数的后面，否则报错
def func(a,b=10)
	r=a+b
	print("和："，r)
func(5)
func(5,5)



2、关键字传参 
在调用参数的时候通过关键字的方式明确指明是给那个参数传值
func(a=100,b=200)
func(b=100,a=200)

装包和拆包
list1=[1,2,3,4,5,6,7,8,9,0]
x,y,*z=list1 #1,2,[3,4,5,6,7,8,9,0]
x,*y,z=list1 #1,[2,3,4,5,6,7,8,9],0
可变参数传参：可变参数args是一个tuple
def add(*args): #加法运算
	sum=0
	for i in args:
		sum=sum+i
	print(sum)
add() # 0
add(1,2,3,4)  # 10
#只要函数定义中出现可变参数，则在使用关键字参数的时候就要慎重
def join(seq,*args): #拼接字符串
	s=""
	for i in args:
		s=s+i
		s=s+seq
	s=s[:-1]
	print("---->",s)
def func1(*args,a=10):#不建议这样写函数
	print(args)
	print(a)
func1(1,2,3,4,5) #(1,2,3,4,5)  10    函数的所有实际参数都无法传递给a 
func1(1,2,3,4,5,a=9)  #(1,2,3,4,5) 9

def func2(*args,**kwargs): #位置参数(可变参数)会放到args(元组),关键字参数会放到kwargs(字典)里
	print(args)
	print(kwargs)  #用来接收关键字参数
func2(1,2,3,a=4,b=5) #(1,2,3)  {4,5}
func2(list1,100) # ([1,2,3,4,5,6,7,8,9,0],100)
func2(*list1,100) # (1,2,3,4,5,6,7,8,9,0,100)



3、混合形式传参
# * 代表之后所有参数传参时必须使用关键字传参
def health_check(name,age,* ,height,weight)
	pass
health_check(name=”zhang”,age=32,height=110,weight=50)


序列传参（使用较少）
def calc(a,b,c)
	return a+b+c
l=[1,2,3]
calc(*l)

字典传参（使用较多）
def calc(a,b,c)
	return a+b+c
dict1={“a”:1,”b”=:2,”c”:3}
calc(**dict1)

返回值包含多个数据(python独有)
list1=[1,2,3,4,5,6,100,7,8,9]
def func(l):
	if isinstance(l,list):
		max=l[0]
		index_max=0
		for index,i in enumerate(l):
			if i>max:
				max=i
				index_max=index
	return max,index_max
r=func(list1)
print(r) # (100, 6)
def get_detail_info():
	dict1={
		"employee":[
		{"name":"张三","salary":1800},
		{"name":"李四","salary":2000},
	],
	"device":[
		{"id":"8837120","titile":"xx笔记本"},
		{"id":"8837121","titile":"xx台式机"},	
	],
	"asset":[{},{}],
	"project":[{},{}],
	}
	return dict1
r=get_detail_info()
print(r) #{'employee': [{'name': '张三', 'salary': 1800}, {'name': '李四', 'salary': 2000}], 'device': [{'id': '8837120', 'titile': 'xx笔记本'}, {'id': '8837121', 'titile': 'xx台式机'}], 'asset': [{}, {}], 'project': [{}, {}]}
4、函数之间的调用
例子1：
books=['红楼梦','西游记','水浒传','三国演义']
def show_books():
	print("---图书馆书记如下")
	for index,book in enumerate(books):
		print("{}:{}".format(index+1,book))

def add_book(book_name):
	if books:
		books.append(book_name)
		show_books()
	else:
		print("书籍不能为空")

add_book("背影")
例子2：
def func1(a):
	for i in range(a):
		print(i)
def func2():
	ran=random.randint(1,5)
	func1(ran)
func2()


5、python内存管理中的intern机制，字符串驻留机制
当字符串处于不同代码块中时，符合字符串格式要求的话，就会开启 intern 机制，
此机制对应于 LEGB 不同的作用域才会开启。
L：local 本地 局部作用域
E：enclosing 嵌套作用域（外部函数变量）
G：global 全局作用域
B：builtins 所有py文件执行的时候都会加载的内置模块

#全局变量
books=['红楼梦','西游记','水浒传','三国演义']
member=10

def func3():
	books.append("背影") #因为books是可变类型，可以省略global声明
	global member   #因为member是不可变类型，所以在函数中想修改则必须添加glo	bal声明
	member+=1

a=200
def func4():
	a=10   # enclosing
	b='good'
	c=[1,3,5,7]
	def inner_func():
		a=100
		print("我是一个内部函数",a) #我是一个内部函数 100

	inner_func()

	print(locals()) 
#{'a': 10, 'b': 'good', 'c': [1, 3, 5, 7], 'inner_func': <function func4.<locals>.inner_func at 0x00000277323820D0>}

print(globals())
#{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002DD900E2910>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'D:/python学习资料/django学习-code/myshop-back/apps/basic/tests.py', '__cached__': None, 'TestCase': <class 'django.test.testcases.TestCase'>, 'copy': <module 'copy' from 'D:\\envs\\myshopback\\lib\\copy.py'>, 'random': <module 'random' from 'D:\\envs\\myshopback\\lib\\random.py'>, 'Iterable': <class 'collections.abc.Iterable'>, 'a': 200, 'func4': <function func4 at 0x000002DD900C71F0>}
func4()

a = 100
b = 0
def func5(b):
    a = 10
    def inner_func(c):
        # nonlocal b  #nonlocal表示外部函数的变量,可修改外部函数的不可变类型的变量
        global b  # 关键字global表示全局变量
        c = a + b + c
        b = c
        print(a)  # 10
        print(b)  # 15

    print(a)  # 10
    print(b)  # 8

    inner_func(5)
    print(b)  # 8


func5(8)


搜索变量的规则线：
1、如果有内部函数，先找内部函数自身的变量
2、如果内部函数没有变量，则找外部函数的变量
3、如果外部函数也不存在此变量则找全局
4、如果全局也没有此变量，则找builtins
5、如果内部builtins也没有则报错

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6}


def func(set1, set2):
    # global set2       # SyntaxError: name 'set2' is parameter and global
    set2 = set1 & set2
    print(set2)


func(set1, set2)



