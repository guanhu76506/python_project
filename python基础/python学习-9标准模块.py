builtins #系统默认加载的模块
print(ord("A")) # 65
print(ord("中")) #20013
print(chr(123456))
"""
os负责程序与操作系统的交互，提供程序访问操作系统底层的接口
sys主要负责程序与python解析器的交换，提供一系列函数与变量，用于操控pyhton的运行环境。
"""
1、os
mkdir() 
rmdir() #可以删除空的文件，删除非空文件夹触发OSError
shutil.rmtree(r'E:\新建文件夹')  #非空文件夹的删除(递归删除)

# 传入任意一个path路径，返回的是该路径下所有文件和目录组成的列表；
print(os.listdir(r"D:\selenium_python"))
os.chdir(path)		#切换目录
os.getcwd() #获取当前文件目录的绝对路径
print(os.getlogin())  # 获得当前系统登录用户名称：Administrator
print(os.cpu_count()) # 获得当前系统的CPU数量：4
# 获得10个字节长度的随机字符串，通常用于加解密运算
print(os.urandom(10)) # b'\x8d\x12[\x85!\xdf\xd8\xb6[P'
os.getpid() #get process id
os.getppid() #get parent process id 获取父进程id


2.os.path
os.environ['os'] # Windows_NT
print(os.path.abspath(r"image\test001.png")) # D:\selenium_python\image\test001.png
# 归一化path的表现形式
print(os.path.normpath(r"D:\selenium_python"))
# 返回当前程序与文件之间的相对路径(relative path)
print(os.path.realpath(r"新建文件夹.txt")) # D:\selenium_python\新建文件夹.txt
print(os.path.isabs(r"image\test001.png"))#False
print(os.path.isfile(r"image\imooc.png"))#True
print(os.path.isdir(r"image")) #True
print(os.path.exists(r"image\imooc.png")) #True
print(os.path.join(os.getcwd()+r"\image\test001.png"))
file_path=r"D:\selenium_python\image\imooc.png"
print(os.path.split(file_path)[1])  # 获取文件名 imooc.png
print(os.path.getsize(file_path))   # 单位为字节
print(os.path.getatime(file_path))  # 文件访问时间
print(os.path.getctime(file_path))  # 文件创建时间
print(os.path.getmtime(file_path) ) # 文件修改时间

os.path.dirname(file_path) #返回目录名称
os.path.basename(file_path) #返回file_path中最后的文件名称


3.time
time.sleep(5)
print(time.time()) #时间为秒的形式 1665895473.265429
st=time.localtime() #返回一个元祖
#time.struct_time
# (tm_year=2022, tm_mon=10, tm_mday=16, tm_hour=12, tm_min=45, tm_sec=40, tm_wday=6, tm_yday=289, tm_isdst=0) 
# <class 'time.struct_time'>
print(st,type(st))
print(st.tm_yday) #289

print(time.asctime(st)) # Sun Oct 16 12:45:40 2022
print(time.strftime('%Y-%m-%d %H:%M:%S',st)) #格式化一个时间 2022-10-16 12:45:40

4.datetime
datetime有4个类：date time timedelta(时间差) datetime
from datetime import datetime
print(datetime.now()) #2022-10-16 13:01:58.518650
print(datetime.today()) #2022-10-16 13:01:58.518650
print(datetime.utcnow()) #世界标准时间 2022-10-16 05:01:58.518650
dt=datetime(2022,8,12,11,11,12)
print(dt) #2022-08-12 11:11:12
print(dt.year) #2022

from datetime import date
from datetime import time
print(date.today()) #2022-10-16
t=time(11,12,48)
print(t,t.hour,t.minute,t.second) #11:12:48 11 12 48

dt=datetime.now()
print(dt) #2022-10-16 12:58:34.586059
from datetime import timedelta

tdt=timedelta(days=1,minutes=1) #时间差,目前时间加上1天30分钟
print(dt+tdt) #2022-10-17 12:59:34.586059

5 sys
#sys.version_info(major=3, minor=8, micro=2, releaselevel='final', serial=0)
print(sys.version_info)
# 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
print(sys.version)
# ['d:\\selenium_python\\test', 
# 'D:\\Program Files (x86)\\python3.8.2\\python38.zip', 
# 'D:\\Program Files (x86)\\python3.8.2\\DLLs', 
# 'D:\\Program Files (x86)\\python3.8.2\\lib', 
# 'D:\\Program Files (x86)\\python3.8.2', 
# 'D:\\Program Files (x86)\\python3.8.2\\lib\\site-packages']
print(sys.path)
def func(a,b):
    return a/b
if __name__=="__main__":
    try:
        func(5,0)
    except Exception as e:
        print(sys.exc_info()) 
        traceback.print_exc(file=sys.stdout)
#sys.exc_info()返回的值是一个元组：
# (<class 'ZeroDivisionError'>, 
# ZeroDivisionError('division by zero'), 
# <traceback object at 0x000002BF5A640980>)
        
"""sys.exc_info()返回的值是一个元组，其中第一个元素
exc_type是异常的对象类型
exc_value是异常的值
exc_tb是一个traceback对象,对象中包含出错的行数、位置等数据。
"""
# sys.argv #命令行参数List，第一个元素是程序本身路径
# sys.modules.keys() #返回所有已经导入的模块列表
# sys.exit(n) #程序，正常退出时exit(0)
# sys.hexversion #获取Python解释程序的版本值，16进制格式如：0x020403F0
# sys.maxint #最大的Int值
# sys.maxunicode #最大的Unicode值
# sys.modules #返回系统导入的模块字段，key是模块名，value是模块
# sys.platform #返回操作系统平台名称
# sys.stdout #标准输出
# sys.stdin #标准输入
# sys.stderr #错误输出
# sys.exc_clear() 	#用来清除当前线程所出现的当前的或最近的错误信息
# sys.exec_prefix 	#返回平台独立的python文件安装的位置
# sys.byteorder #本地字节规则的指示器，big-endian平台的值是'big',little-endian平台的值是'little'
# sys.copyright 		#记录python版权相关的东西
# sys.api_version 	#解释器的C的API版本
# sys.getwindowsversion #获取Windows的版本
# sys.getdefaultencoding #返回当前你所用的默认的字符编码格式
# sys.getfilesystemencoding #返回将Unicode文件名转换成系统文件名的编码的名字
# sys.setdefaultencoding(name) #用来设置当前默认的字符编码
# sys.builtin_module_names 	#Python解释器导入的模块列表
# sys.executable 	#Python解释程序路径
# sys.stdin.readline 	#从标准输入读一行，sys.stdout.write("a") 屏幕输出a


4.calendar
calendar.calendar(2022)
calendar.month(2019,8)
calendar.weekday(2022,8,12)

5.random
random.randint(a,b) # 包含a,也包含b
random.randrange(a,b) # 包含a,不包含b
random.random() #[0,1)
random.choice('abcdefghijklmn') #随机选取一个值
list1=[1,2,3,4,5,6,7,8,9]
random.shuffle(list1)  #洗牌，打乱序列顺序

list2=random.sample('1234567890abcdefghijklmn',8)
print(list1) # ['j', '9', 'f', '7', '1', '5', 'i', 'd']
user_info = ''.join(list2)
print(user_info)  # j9f715id,获取8位随机数


6.math
math.ceil(9.12)
math.floor(9.89)
math.fmod(10,3) #求余
math.fabs(-1) # 1.0
math.sqrt(9)
math.pow(2,5)
print(round(100.123456,4)) #100.1235 系统的四舍五入，math没有四舍五入的方法


7.hashlib
md5=hashlib.md5()
s='明天早上5点发起进攻'
md5.update(s.encode('utf-8'))
print(md5.digest()) # b'\xe4\n\xf1\x1bC\xea\xac\xd9\xee\xccjl\xf8o\x9d|'
print(md5.hexdigest()) # e40af11b43eaacd9eecc6a6cf86f9d7c

sha1=hashlib.sha1(s.encode('utf-8'))
print(sha1.hexdigest(),len(sha1.hexdigest())) 
#7706f1af356559906f61770c5e2a6629b72ebfdf 40
sha256=hashlib.sha256(s.encode('utf-8'))
print(sha256.hexdigest(),len(sha256.hexdigest())) 
# 2c0ae56217f30a2631017814668def1db4f7b7bfbad64cadaa426a355925d7b7 64



8.logging
# 1、日志对象
logger=logging.getLogger()
# 2、设置级别
logger.setLevel(logging.ERROR)
# 3、创建一个handle对象
file='t2/log.txt'
handler=logging.FileHandler(file)
handler.setLevel(logging.ERROR)

# 4.创建一个formatter格式对象
fat=logging.Formatter('%(asctime)s - %(module)s -%(filename)s[%(lineno)d] - %(levelname)s:%(message)s')
handler.setFormatter(fat)

# 5.添加handler对象
logger.addHandler(handler)

def func()
	try:
		num=int(input("请输入一个数字"))
		for i in range(num):
			print('--------->',i)
	except:
		logger.error('输入的不是一个数字')
	finally:
		print('---------over----------')

		

9.urllib和urllib3
import urllib.request
import urllib.parse

url='http://www.baidu.com'
header={}
header['User-Agent']='Mozilla/5.0(Windows NT 6.1...)...'
data={}
data['nav']=0
data=urllib.parse.urlencode(data).encode('utf-8')
# 创建请求对象
request=urllib.request.Request(url,data,header)
response=urllib.request.urlopen(request) # 得到response对象
content=response.read() # 获得字节信息
content.decode('utf-8')	# 对信息进行解码


10.re
import re
"""
re.I re.IGNORECASE 不区分大小写的匹配
re.L re.LOCALE    根据所使用本地语言环境通过\w \W \b \B \S \s实现匹配
re.M re.MULTILINE ^和$分别匹配目标字符串中行的起始和结尾，而不是严格
				  匹配整个字符串本身的起始和结尾
re.S re.DOTALL   "."(点号)通常匹配了除\n(换行符)之外的所有单个字符；
				  该标记表示"."(点号)能够匹配的全部字符
re.X re.VERBOSE	  通过反斜杠转义，否则所有空格加上#(以及在改行中所有
				  后续文字)都被忽略，除非在一个字符类中或者允许注释
				  并且提高可读性

match对象方法:
search() 只要在字符串中找到匹配的就不会继续查找
findall() 查找所有匹配的内容，返回的是一个列表
"""
# 通过re模块的compile，返回一个pattern对象
pattern=re.compile("abc") 
print(pattern) #re.compile('abc')
print(type(pattern)) #<class 're.Pattern'>
print(pattern.pattern) # abc
print(dir(pattern))
"""dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
带参数时，返回参数的属性、方法列表。
['__class__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
'__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
'findall', 'finditer', 'flags', 'fullmatch', 'groupindex', 'groups', 
'match', 'pattern', 'scanner', 'search', 'split', 'sub', 'subn']
"""

# 通过pattern对象 match search findall split
match_obj=pattern.match('abcdef')
print(match_obj) # <re.Match object; span=(0, 3), match='abc'>
print(match_obj.string) #abcdef
print(match_obj.re) #re.compile('abc')
g=match_obj.group() # 匹配对象通过group获取匹配的内容
print(g) # abc


match_obj2=re.match('abc','ABCdef',re.I)
match_obj3=re.fullmatch('abc','ABCdef',re.I)
# search()方法只查找一次就返回结果，不会继续查找了
match_obj4=re.search('abc','ABCdef',re.I)
print(match_obj2.group())
print(match_obj2.span())
print(match_obj2.start())


s="one1two12three33four444five5six698"
# 该方法将字符串中的数字替换成number，onenumbertwonumberthreenumberfournumberfivenumbersixnumber
s=re.sub(r'\d+','number',s) 

def change(mobj): #该方法可使字符串里的数字部分都加1
	result = mobj.group()
    result=str(int(result)+1)
    return result
s=re.sub(r'\d+',change,s) 
"""sub(replacement, string[, count=0])
replacement是被替换成的文本
string是需要被替换的文本
count是一个可选参数,指最大被替换的数量
"""
p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes'))
print(p.sub('colour', 'blue socks and red shoes', count=1))
#colour socks and colour shoes
#colour socks and red shoes
# subn()方法执行的效果跟sub()一样，返回一个元组，包括替换后的新的字符串和总共替换的数量
q = re.compile('(blue|white|red)')
print(q.subn('colour', 'blue socks and red shoes'))
print(q.subn('colour', 'blue socks and red shoes', count=1))
# ('colour socks and colour shoes', 2)
# ('colour socks and red shoes', 1)
print(type(q))  # <class 're.Pattern'>

#邮箱:126,163,qq,必须符合也邮箱的格式
email=input("请输入邮箱")
m_obj=re.search(r'^(\w{4,16})@(126|163|qq).com',email)
if m_obj:
	email_name=m_obj.group(1)
	print(email_name+'符合邮箱格式')
else:
	print('不符合邮箱格式')

#电话: 1开头，不是以4,7结尾的手机号码(11位) 或者010-3456789 0123
tel=input('输入手机号码')
m_obj=re.fullmatch(r'1\d{9}[0-35689]|\d{3,4}-\d{7,8}',tel)
print(m_obj)


#使用()进行分组,使用\number进行反向引用
html=r'<div><a href="http://www.baidu.com">百度</a></div>'
m=re.fullmatch(r'<(.+)><(.+) href="http://www.baidu.com">.+</\2></\1>',html)
print(m.group(1)) # div
print(m.group(2)) # a

#分组命名的方式(?p<name>pattern)
html=r'<div><a href="http://www.baidu.com">百度</a></div>'
m=re.fullmatch(r'<(?P<outer>.+)><(?P<inner>.+) href="http://www.baidu.com">.+</(?P=inner)></(?P=outer)>',html)
print(m) #<re.Match object; span=(0, 48), match='<div><a href="http://www.baidu.com">百度</a></div>'>
print(m.group(1)) # div
print(m.group(2)) # a
print(m.groups()) #('div', 'a')

#贪婪匹配：在整个表达式匹配成功的前提下,尽可能多的匹配 例如：s='abbbbbc'  ab+
#非贪婪(Non-greedy)匹配：在整个表达式匹配成功的前提下,以最少的字符匹配 例如：ab+?
*?,+?,?? Non-greedy versions of the previous three special characters.
{m,n}?   Non-greedy version of the above.
s='abbbbbc'
m=re.match('ab+?',s)
print(m.group())
#############################################################
# 找出字符串中的数字
content='one1two12three33four444five5six698'
# 使用编译的对象
p=re.compile(r'[a-z]+',re.I)
rest=p.findall(content)
print(rest) # ['one', 'two', 'three', 'four', 'five', 'six']
all_rest=re.findall(r'[a-z]+',content,re.I)
print(all_rest) # ['one', 'two', 'three', 'four', 'five', 'six']

#############################################################
s='one1two12three33four444five5six698'
p=re.compile(r'\d+') 
print(p) # re.compile('\\d+')
rest=p.split(s,2) #使用split分割字符串
print(rest) # ['one', 'two', 'three33four444five5six698']

######################################################
def test_group():
    content = 'hello, world!'
    p = re.compile(r'world')
    print(rest) # <re.Match object; span=(7, 12), match='world'>
    if rest:
        # group的使用
        print(rest.group()) #world
        # groups的使用
        print(rest.groups()) #()


def test_id_card():
    """ 身份证号码正则匹配 """
    # p = re.compile(r'(\d{6})(\d{4})((\d{2})(\d{2}))\d{2}(\d{1})([0-9]|X)')
    p = re.compile(r'(\d{6})(?P<year>\d{4})((?P<month>\d{2})(?P<day>\d{2}))\d{2}(\d{1})([0-9]|X)')
    # 准备两个身份证号码
    id1 = '430656199610015493'
    id2 = '43065619961001548X'
    rest1=p.search(id2)
    print(rest1.group()) # 43065619961001548X
    # 月，日
    print(rest1.group(4)) # 10
    print(rest1.group(5)) # 01
    # groups
    print(rest1.groups()) # ('430656', '1996', '1001', '10', '01', '8', 'X')
    # groupdict
    print(rest1.groupdict()) # {'year': '1996', 'month': '10', 'day': '01'}

#############################################################################
content = 'hello, world!'

p = re.compile(r'world')
"""math vs search
#match() 如果在字符串的开头有0个或更多个字符，符合正则表达式模式，
返回相关匹配的实例对象，如果字符串不符合正则表达式模式则返回None；
#而search()则不同，扫描整个字符串，如果产生了一个匹配正则模式就寻找到这个位置，
返回相关匹配的对象。如果没有位置能够匹配这个模式则返回None
"""
# 使用search
rest = p.search(content)
print(rest) # <re.Match object; span=(7, 12), match='world'>

# 使用match
rest_math = p.match(content)
print(rest_math) # None



# 使用函数进行调用
rest_func = re.search(r'world', content)
print(rest_func) # <re.Match object; span=(7, 12), match='world'>

######################################################
# 使用正则表达式进行替换 replace

s = 'one1two2three3333four4five5six6'
# one@two@three@four@five@six@

# 使用正则替换
p = re.compile(r'\d+')
rest = p.sub('@', s)
print(rest)

# 使用字符串原始的替换方式
rest_origin = s.replace('1', '@').replace('2', '@').replace('3333', '@')
print(rest_origin)


# 使用正则表达式跟换位置
s2 = 'hello today'
p2 = re.compile(r'(\w+) (\w+)')
rest_pos = p2.sub(r'\2! \1', s2)
print(rest_pos)


# 在原有的内容基础上，替换并改变内容
def f(m):
    """ 使用函数进行替换规则改变 """
    return m.group(2).upper() + ' ' + m.group(1)


rest_change = p2.sub(f, s2)
print(rest_change) # TODAY hello


# 使用匿名函数进行替换 lambda
rest_lamb = p2.sub(lambda m: m.group(2).upper() + ' ' + m.group(1), s2)
print('----------')
print(rest_lamb) # TODAY hello
