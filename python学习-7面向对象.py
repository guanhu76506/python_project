"""	类与对象：
	属性：
		类属性：在类的空间中，既可以被类访问，也可以被对象访问
		对象属性：在对象的空间中的属性，只能被当前的对象访问
	创建方式一：
		类属性：
			class 类名:
				属性=值   --->  类属性
			对象属性：
				步骤：
					1.创建对象：	对象=类名()
					2.对象.属性名=值    ----->  在空间中添加了对象属性
	方式二：
		依赖__init__()完成 		
		在__init__(self)方法中完成所有对象属性的统一，其中self表示对象本身
"""

"""	封装：
	1.属性和方法  --->  封装到类中
	2.属性封装	将属性私有化，并定义公有set和get方法

	私有化：只能类自身中进行调用，实现属性或方法的私有化要通过: __属性名,__方法名()
	python底层对私有属性方法进行了改名操作: _类名__属性名,_类名__方法名()
	私有化作用：
		1.隐藏属性，只能在类中使用
		2.对私有属性的赋值和取值起到一定的限制作用
		3.通过set方法限制赋值，通过get方法限制取值	
"""

class Person:
    # 限制作用
    #__slots__:为指定的类设置一个静态属性列表，为属性很少的类节约内存空间。
    __slots__ = ['__name', '__age', '__flag']
    # 初始化魔术方法,初始化对象时触发(不是实例化触发,但是和实例化在一个操作中)
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__flag = True
    """	@property 装饰器用来装饰类中的方法  步骤：	
	1.在get方法上面添加#@property 装饰器，函数的名字最好更加简要，让使用者在调用
	或者访问的时候更加简单
	2.装饰set方法：
		@属性名.setter
		def 属性名(self,参数)
			pass
	3.使用：
		对象=类名(参数)
		对象.属性名  ---> get方法
		对象.属性名=值  	--->set方法
    """
    @property    
    def get_name(self):
        if self.__flag:
            return self.__name
        else:
            print('没有权限查看用户名，获取失败')

    @get_name.setter
    def set_name(self, name):
        if len(name) > 6:
            self.__name = name
        else:
            print("名字必须大于等于6位")



"""
类方法		可以通过类名调用也可以通过对象调用 
静态方法		可以通过类名调用也可以通过对象调用

类方法和静态方法里不能调用普通方法
"""
class Utils:
	# 类属性
	version='1.0'
	# 类方法  类方法中不能访问对象属性
	@classmethod
	def conn_db(cls,version): #cls就是类对象本身
		print('---类方法',cls.version)
		

	# 静态方法	
	@staticmethod
	def select_data():
		print(Utils.version)

	def show():
		print('普通方法')

u=Utils()
Utils.select_data()
print('*'*50)
print(u.show())

""" 魔术方法就是一个类的特殊方法，和普通方法唯一的不同是，普通方法需要调用，
    而魔术方法需要系统调用。
"""
class PersonX:

	def __init__(self,name,age):
		self.name=name
		self.__age=age


	""" 实例化魔术方法(类方法),在实例化对象时触发,必须返回一个对象实例
		注意：实例化对象对象是Object类的底层实现,其它类继承了Object的__new__才能够
		实现实例化对象。没事别碰这个魔术方法，先触发__new__才会触发__init__
	"""		
	def __new__(cls, *args, **kwargs):
        print('---------->new')
        obj=object.__new__(cls)
        return cls #返回一个对象实例
    """
		析构魔术方法：当对象没有用(没有任何变量引用)的时候触发
		在销毁对象时回收资源
		注意：del不一定会触发当前方法，只有当前对象没有任何变量引用时才会触发
    """
    def __del__(self):
    	print('---------->del')
    """
		使用print(对象)或者str(对象)时触发
		返回值必须是字符串类型
    """
   	def __str__(self):
   		return self.name+str(self.age)

   	# 在使用repr(对象)时触发，返回值必须是字符串类型
   	def __repr__(self):
   		return "hi"
   	"""调用对象的魔术方法 
   		将对象当做函数调用时触发，方式:对象()	返回值：根据情况而定
		作用:可以将复杂的步骤进行合并操作，减少调用的步骤
   	"""
   	def __call__(self, *args, **kwargs):
   		return "hello world"
   	# 返回对象的长度
   	def __len__(self):
   		return 5
   	# 运算相关的魔术方法: __gt__,__lt__,__eq__,__ge__,__le__等等
   	def __gt__(self,other):
   		return self.age>other.age
   	# 属性操作相关魔术方法: __getattr__,__setattr__
   	def __getattr__(self,item):
   		if item=='age':
   			return 20
   		elif item=='gender':
   			return '男'
   		else:
   			return '不存在此属性{}'.format(item)

   	def __setattr__(self,key,value):
   		print(key,value)
   		if key=='phone' and value.startswith('139'):
   			#self.key=value  #递归了，不能这么写
   			object.__setattr__(self,key,value)  		
   				
p=PersonX('zhangsan',22)
print(p)	#<__main__.PersonX object at 0x0000025B4242FDC0>
# 获取p对象的自身属性，并以字典的形式返回
print(p.__dict__) 	# {'name': 'zhangsan', '_PersonX__age': 22}
print(p()) 		#hello world
del p


"""继承：使程序代码更加简练，提高可读性
		子类继承了父类的非私有属性和方法，公有的属性和方法是可以直接在子类中访问的，
		但是私有的方法是无法访问到的
	1.定义一个父类
	2.定义子类继承父类
		a.继承父类非私有化的属性和方法
		b.如果子类定义了一个跟父类相同的属性，先找子类的属性，然后找父类的
		c.如果父类与子类有相同的方法，则认为子类重写(override)了此方法

	多重继承：类的多重继承（继承多个类时，不要有重名方法，方便维护）
	class 类名(父类1，父类2):
		pass
	搜索顺序： 可查看:类名.__mro__,类名.mro()
"""

class Student(Person):
	def __init__(self):
		print("------>Student init")

class Teacher(Person):
	def show(self):
		self.name
		self.age
		self._Person__money

class Admin(Person):



class Anaimal:
	type1='动物'
	def __init__(self):
		print('---->Anaimal')
	def run(self):
		print('喜欢跑')
	def eat(self):
		print('喜欢吃')
    def __str__(self):
    	return '当前类型：{}'.format(Anaimal.type1)

class Dog(Anaimal):
	type1='狗'
	def __init__(self,name,color):
		Anaimal.__init__(self)
		self.name=name
		self.color=color

	def see_home(self):
		print('看家高手')

    def eat(self):
    	# super(Dog,self).eat() #子类方法中调用父类的方法 方式1
    	Anaimal.eat(self)		#子类方法中调用父类的方法 方式2
    	print('可以啃骨头')
d=Dog('大黄','黄色')  
d.run() 
d.see_home()
print(d) 
print(Dog.mro())	
# [<class '__main__.Dog'>, <class '__main__.Anaimal'>, <class 'object'>]
print(Dog.__mro__)
# (<class '__main__.Dog'>, <class '__main__.Anaimal'>, <class 'object'>)


# 多态:每当无需知道对象是什么样的就能对其操作时，都是多态在起作用。
# 同一个方法在不同的类中，呈现不同的结果
class PetShop:
	def __init__(self,name):
		self.name=name
		self.pets=[]

	def save_pet(self,pet):
		if isinstance(pet,Pet):
			self.pets.append(pet)
			print('添加成功')
		else:
			print('不是宠物不收留')

	def sale_pet(self,pet):
		if isinstance(pet,Pet):
			self.pets.remove(pet)
			print('宠物减少')
		else:
			print('不是宠物不收留')

	def search_pet(self,pname):
		for pet in self.pets:
			if pname==pet.pname:
				print('宠物在商店')
				break
			else:
				print('不存在此宠物')

	def all_pets(self):
		print('宠物店所有的宠物信息如下：')
		for pet in self.pets:
			print(pet)


class Pet:
	type='宠物'

	def __init__(self,pname,color,age):
		self.pname=pname
		self.color=color
		self.age=age

	def __str__(self):
		return '当前类型是：{}，宠物名是：{}'.format(self.type,self.pname)

class Dog(Pet):
	type='狗'

	def see_hourse(self):
		print('特长看家')

class Cat(Pet):
	type='猫'

	def catch_mouse(self):
		print('抓老鼠')

print(type(Cat))		#<class 'type'>
shop=PetShop('爱宠')

cat=Cat('花花','黄色',2)
shop.save_pet(cat)
dog=Dog('大黄','棕色',3)
shop.save_pet(dog)

shop.all_pets()


# 类装饰器
class decorator:
	def __init__(self,func):
		self.func=func
		print(func.__name__)	#girl
	def __call__(self,*args,**kwargs):
		self.func(*args,**kwargs)
		print('涂点粉')
		print('涂口红')
		print('变成小萝莉')
@decorator
def girl():
	print("俺是大妈")

girl()

##########################################################
class decorator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __call__(self, *args, **kwargs):
        class inner_class:
            def __init__(self,func):
                self.func=func
                print(self.func.__name__) 	#girl
                print(self.func.__doc__)	#None

            def __call__(self, *args, **kwargs):
                self.func(*args, **kwargs)
                print('涂点粉')
                print('涂口红')
                print('变成小萝莉')
                
        return inner_class(*args)
@decorator("hhhhhh",666666)
def girl():
    print("俺是大妈")
girl()

###################################################################
# 类的装饰器，可以对类的方法进行扩充
def eat(cls):
	cls.eat=f
	return cls
def f(self):
	print('{},hello'.format(self.name))
	print('6666666666')

@eat
class Cat():
	def __init__(self,name):
		self.name=name

cat=Cat('小白')
cat.eat()


# 元类type,类也是对象，他们的类型是type
print(type(int)) 		#<class 'type'>
Student = type('Student', (object,), {'type': '学生类'}) #调用元类可以创建类
print(type(Student))	#<class 'type'>

############################################################
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):

        print(name) #MyList
        print(bases) #(<class 'object'>,)
        #{'__module__': '__main__', '__qualname__': 'MyList', 'a': 'hello'}
        print(attrs)
        attrs['b']='world'
        # if attrs.get("test"):
        #     attrs.pop("test")
        return type.__new__(cls,name, bases, attrs)


class MyList(object,metaclass=ListMetaclass):
    a = 'hello'
    # def test(self):
    #     print("-----")
    #'test': <function MyList.test at 0x000001AC1595FCA0>


x = MyList()
print(x)	#<__main__.MyList object at 0x000001AC123BFDC0>
print(x.a)
print(x.b)
#print(x.test)

###############################################################
# 单例类 singleton
class Person:
	__instance=None

	def __new__(cls,*args,**kwargs):
		if cls.__instance is None:
			cls.__instance=object.__new__(cls,*args,**kwargs)
		return cls.__instance

	def __init__(self):
		pass

p1=Person()
p2=Person()
p3=Person()
print(p1,id(p1))
print(p2,id(p2))
print(p3,id(p3))
#输出结果：
<__main__.Person object at 0x000001F35D775790> 2144756782992
<__main__.Person object at 0x000001F35D775790> 2144756782992
<__main__.Person object at 0x000001F35D775790> 2144756782992
####################################################################
# 单例类装饰器的实现
class cls_decorator:
	def __init__(self,f):
		self.f=f
		self.__instance={}

	def __init__(self,*args,**kwargs):
		if self.f not in self.__instance:
			self.__instance[self.f]=self.f()
		return self.__instance[self.f]

@cls_decorator
class Singleton:
	def __init__(self):
		print("------>Singleton init")

print(Singleton) #<__main__.cls_decorator object at 0x0000019B83CD09A0>
s1=Singleton()	#------>Singleton init
s2=Singleton()
print(s1 is s2) #True

########################################################################
# 函数装饰器实现
def func_decorator(cls):
	_instance={}

	def wrapper(*args,**kwargs):
		if cls not in _instance:
			_instance[cls]=cls()
		return _instance[cls]
	return wrapper

class Singleton:
	def __init__(self):
		print('Singleton init')
@func_decorator
print('Singleton')


#########################################################################
"""异常处理
	try:
		# 可能出现的异常代码
	except ValueError as e:
		print(e) #如果存在异常执行的代码
	except TypeError as e:
		print(e) #如果存在异常执行的代码
	excepy Exception as e:
		print(e) #如果存在异常执行的代码
	else:
		print('') #没有遇到异常时执行的代码
	finally:
		#无论是否存在异常都会执行的代码部分

	如果代码有返回值+finally，则肯定会执行finally里面的代码部分
"""
# 自定义异常
class UserNameError(Exception):
	def __init__(self,*args,**kwargs):
		pass

class PasswordError(Exception):
    def __init__(self, *args, **kwargs):
        pass

def register():
	username=input("请输入用户名")
	if if len(username)<6 or username[0].isdigit():
		raise UserNameError('用户名格式错位')
	else:
		password = input(("请输入密码"))
        if 10 > len(password) > 6:
            print('密码合法')
        else:
            raise PasswordError("密码不合法")

register()