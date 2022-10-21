
1、	python基础
1.1 python变量和字符串
""" python关键字 help('keywords')
False class from or None continue global pass True def if raise and del 
import return as elif in try assert else is while async except lambda 
with await finally nonlocal yield break for not
"""
type函数用于得到变量的数据类型
b1 = b'hello'
print(b1)  # b 'hello's
print(type(b1))  # <class 'bytes'>
print("口", end="")  # 结尾不换行
# objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用","分隔。
# sep -- 用来间隔多个对象，默认值是一个空格。
# end -- 设定以什么结尾。默认值是换行符\n，可以换成其他字符串；“end=' '”指末尾不换行，加空格。
# file -- 要写入的文件对象。
# flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新。



# help(os.path) 查看python帮助文档
# help('modules')
# help('modules yourstr')
# help('str.find')
# help('open')
print(1 == 1.0)  # True
print(1 not in [1, 2, 3, 4])
print(5 + 6 if 5 > 6 else 5 - 6)

# 枚举
set1={"猫","狗","老鼠"}
for index,value in enumerate(set1):
	print("{},{}".format(index,value))
else:
	print("----over----")
#输出结果
0,老鼠
1,猫
2,狗
----over----
	
count=0
while count<5:
	print("hello")
	count+=1
	if(count==3):
		break
else:
	print("-------")
循环体里的break语句执行了的话，esle语句就不会执行



#使用str能以合理的方式将值转换为用户能够看懂的字符串。尽可能将特殊字符编码转换为相应的字符。
#然而，使用repr时，通常会获得值的合法Python表达式表示。
>>> print(repr("Hello,\nworld!"))
'Hello,\nworld!'
>>> print(str("Hello,\nworld!"))
Hello,
world!


复数类型：complex
a=5+8j
a.conjugate()   #复数的共轭
print(type(a))  # <class 'complex'>
print(a.real,a.imag) # 实数部分和虚数部分别为:5.0, 8.0

1、字符串前加u  例：u"我是含有中文字符组成的字符串。"
作用：后面字符串以Unicode格式进行编码，一般用在中文字符串前面，
防止因为源码储存格式问题，导致再次使用时出现乱码。
2、字符串前加 r
例：r"\n\n\n\n"表示一个普通生字符串 作用：去掉反斜杠的转移机制。
应用：常用于正则表达式，对应着re模块。
3、字符串前加b 例: response = b'Hello World!' 
b" "前缀表示：后面字符串是bytes 类型。
网络编程中，服务器和浏览器只认bytes 类型数据。
如：send 函数的参数和 recv 函数的返回值都是 bytes 类型
在 Python3 中，bytes 和 str 的互相转换方式是
str.encode('utf-8')
bytes.decode('utf-8')
4、字符串前加f,以f开头表示在字符串内支持大括号内的python表达式
import time
t=time.sleep(1)
print(f'list initial size {sys.getsizeof(t)}')


字符串方法： 
format()函数支持格式化字符串、数字
name = "小明"  age = 25  height = 180.5
str1 = "我叫{0},我在{1}班,身高{3},今年{2}".format(name , "3-2" , age , height)
#我叫小明,我在3-2班,身高180.5,今年25
str1 = "我叫{p1},身高{p4},今年{p3},我在{p2}班".format(p1=name, p3=age , p4=height, p2="3-2")
#数字的格式化
num = 1234567.89555   str4 = format(num , '0.4f')
#1234567.8956
account = "8810381"   amt = 123456789.12345
str5 = format(amt , "0,.3f")
str6 = "请您向" + account + "账户转账¥" + str5 + "元"
#请您向8810381账户转账¥123,456,789.000元
#在字符串格式化输出时，如遇要格式化输出的数字，则需要在{}内增加:前缀，之后写上数字格式化语句
str7 = "请您向{}账户转账¥{:0,.3f}".format(account , amt)
#请您向8810381账户转账¥123,456,789.000
print("请您向%s账户转账¥%0.3f" %(account , amt))

lower() upper() capitalize() title() swapcase() 
lstrip() rstrip() strip()

replace(old,new,count):用new字符串替换old字符串，count表示替换的次数
split():分割字符串,返回一个列表
#str8里面的r 表示原始字符串
str8=r'D:\scapy-master\scapy\modules\krack'
print(str8) #D:\scapy-master\scapy\modules\krack
find()方法获取字符串出现的位置，与index()方法的功能类似。
只不过在没有找到元素，find()返回-1，index()报ValueError
rfind()方法和rindex()方法 从右向左查找字符
没有找到元素，rfind()返回-1，rindex()报ValueError
s_split=str8.split("\\",3)
s_split=str8.split("\\")
s_find=str8.rfind('\\')
str8.center(50)  #居中对齐,50宽度
str8.ljust(50)   #左对齐
str8.rjust(50)
字符串判断相关函数
isupper()
islower()
isalpha() 是否字符串中只有字母组成
isdigit() 是否纯数字
startswith("H") 是否以指定的内容开头
endswith() 


s="abcdefg"
for i in range(0,len(s)):
	letter=s[i]
	print(s[i])
index=0
while index<len(s):
	print(s[index])
	index+=1

# 创建数字序列
r=range(10,20,2) # 10,12,14,16,18
print(12 in range(10,20))

# 切片格式[start:[stop:[step]],三个参数的意义分别起始位置,终止位置和步长


hash()函数
h1=hash("abc")
print(h1)
h2=hash("def")
print(h2)
print(hash(8838183))

1.2运算符
算数运算符：+ 	- 	*	 /	 % 	**	//(整除取整数)
赋值运算符：= += -= *=  …
关系运算符：==(比较内容) >=  <=  !=  > <  
逻辑运算符：and or not   False的情况： '' 0 None
位运算：&  |  ~  ^  >>  <<
成员运算符： in和not in  print(1 not in [1, 2, 3, 4])
身份运算符：is(比较地址) 和is not
三目运算符：print(5 + 6 if 5 > 6 else 5 - 6)
进制：
a=0b101110101 #二进制以0b开头
print(a)      #373
print(oct(a))   #0o565
print(hex(a))  #0x175
print(int('0b1011110111', base=2))  #759

1.3可变与不可变
不可变类型：只要改变变量的值则地址(通过id()方法判断)发生变化，则认为此类型是不可变的。
不可变类型有：string,int,float,tuple,bool
可变类型：内容发生改变，但是地址没有改变，则认为此类型是可变类型。
可变类型有：list,set,dict
dict类型：key,value。Key是不可变的，value是可变的
1.4浅拷贝与深拷贝
拷贝：其实就是将容器内的数据备份一份到新的地址
浅拷贝：可变类型共用的是同一个（里面的内容改变，但是地址不会改变）
不可变类型一开始是共用的。但是如果有发生改变的，则地址就会发生改变
list.copy() copy.copy()
import copy
list1=["张三",20,"男",["足球","篮球","桌球"]]
list2=list1.copy() #浅拷贝
list3=copy.copy(list1) #浅拷贝
print(list1,list2,list3)
print(id(list1),id(list2),id(list3))
['张三', 20, '男', ['足球', '篮球', '桌球']] ['张三', 20, '男', ['足球', '篮球', '桌球']] ['张三', 20, '男', ['足球', '篮球', '桌球']]
2114939336320 2114939336448 2114939402304

list2[3].append("冰球")
print(list1,list2,list3)
print(id(list1),id(list2),id(list3))
['张三', 20, '男', ['足球', '篮球', '桌球', '冰球']] ['张三', 20, '男', ['足球', '篮球', '桌球', '冰球']] ['张三', 20, '男', ['足球', '篮球', '桌球', '冰球']]
2114939336320 2114939336448 2114939402304

list1[3].remove("足球")
print(list1,list2,list3)
print(id(list1),id(list2),id(list3))
['张三', 20, '男', ['篮球', '桌球', '冰球']] ['张三', 20, '男', ['篮球', '桌球', '冰球']] ['张三', 20, '男', ['篮球', '桌球', '冰球']]
2114939336320 2114939336448 2114939402304

list2[0]="李四"
print(list1,list2,list3)
print(id(list1),id(list2),id(list3))
['张三', 20, '男', ['篮球', '桌球', '冰球']] ['李四', 20, '男', ['篮球', '桌球', '冰球']] ['张三', 20, '男', ['篮球', '桌球', '冰球']]
2114939336320 2114939336448 2114939402304
深拷贝：copy.deepcopy()
列表中可变类型的元素会有一个新的地址，而不是像浅拷贝一样共用一个地址
list4 = copy.deepcopy(list1) # 深拷贝
for e in list1:
    print(e,id(e))

for e in list4:
    print(e,id(e))
张三 2584718169744
20 140711782570240
男 2584718245680
['篮球', '桌球', '冰球'] 2584769959552
张三 2584718169744
20 140711782570240
男 2584718245680
['篮球', '桌球', '冰球'] 2584770499520

########################################################################
"""
模块：一个py文件就是一个模块
本模块获取自己的名字：
    __name__  ----->  __main__
其它模块导入获取模块的名字：
    __name__  ----->   模块自身的名字
"""

"""
__init__.py文件中也可以定义一些函数，变量，类
也是一个模块，此模块理解成是"魔术的",只要导入包就会执行此模块

from student.model import Student
from student.views import MAX
步骤：
1.如果有包，先加载包，执行__init__.py文件 只执行一次
2.然后找包中模块，加载模块(执行模块文件)
3.可以使用包中模块的内容了
"""

"""
想导入包的时候加载一些内容，则需要在__init__.py中定义一些内容
from 包名 import *
在其他的模块中通过from 包名 import * 导入则可以使用__init__.py中定义的所有内容

如果想限制__init__.py中的内容访问，则需要结合__all__=[]

__all__=["外界可以访问的内容"]
    外界只能使用列表中的内容

避免循环导入:
1.重构代码
2.将导入的语句放到函数中
"""

###############################################################################
# 单元测试框架 unittest
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(" "), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

    def test_strip(self):
        s='  hello       '
        self.assertEqual(s.strip(),'hello')

    def setUp(self) -> None:
        print('-------------start----------------')

    def tearDown(self) -> None:
        print('------end-----------------------')

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
if __name__ == '__main__':
    unittest.main()


####################################################################
# 文档测试框架 doctest
"""
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""
def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

