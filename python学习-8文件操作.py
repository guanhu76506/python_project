"""文件操作
	open(file,mode)  open file and return a stream
	注意：只要mode='r'读的文件不存在则报错 
	mode模式有：
	'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
"""
#1.访问文件并得到流对象
rstream=open('a.txt')
#2.通过流对象进行读操作
line=rstream.readline()
lines=rstream.readlines() #返回一个列表
all_text=rstream.read()
print(all_text)
#3.释放流对象资源
rstream.close()

####################################################
#使用with语法，到达语句末尾时自动关闭文件，即便出现异常也是如此。
def read_file():
	file_name='test.txt'
	file_path=""
	with open(file_name,encoding='utf-8') as f:
		print(f.read(10))
		print(f.readline())		
		f.seek(20)
		print(f.readline())	
		print(f.readlines())
		print(len(f.readlines()))
read_file()

# 文件写入
# w=open(file_name,'w')
# 方法：write() 	writelines(list)
# 只要是写操作，如果没有此文件，则默认会创建文件
# 使用函数write()向打开的文件对象写入内容
# 使用writelines()函数向打开的文件写入多行内容
def write_mutil_line():
	file_name=""
	with open(file_name,'w',encoding='utf-8') as f:
		l=['1','2','3']
		f.writelines(l)
def write_use_log():
	file_name=""
	str=""
	with open(file_name,'w',encoding='utf-8') as f:
		f.write(str)
def read_and_write():
	file_name=''
	with open(file_name,'w',encoding='utf-8') as f:
		if '1' in f.read():
			f.write('aaa')
		else:
			f.write('bbb')
		f.write("\n")
######################################################################
###用户登录持久化数据
class User(object):
	"""docstring for ClassName"""
	def __init__(self, username,password):		
		self.username = username
		self.password=password
	def __str__(self):
		return self.username

	def login(self):
		self.username=input("用户名")
		self.password=input("密码")
		if self.username and self.password:
			with open('user.txt','r',encoding='utf-8') as rs:
				users=rs.readlines()
				for user in users:
					user=user.replace("\n",'')
					ulist=user.split(' ')
					if self.username=ulist[0] and self.password=ulist[1]:
						print('登录成功')
						return False

					else:
						print("不存在此用户")
		return True

	def register(self):
		self.username=input("用户名")
		self.password=input("密码")
		if self.username and self.password:
			with open('user.txt','a',encoding="utf-8") ws:
				ws.writelines("{} {}\n".format(self.username,self.password))
			print("注册成功")
		else:
			print("用户名或者密码不能为空")

def main():
	flag=True
	u=User()
	u.register()
	while flag:
		print('用户请登录')
		flag=u.login()

main()
############################################################
# 文件的复制
file_path=r""
with open(file_path,"rb") as rstream:
	content=rstream.read()
	# 写入
	filename=file_path[file_path.rfind("\\")+ 1:]
	with open(filename,'wb') as wstream:
		wstream.write(content)
print("复制完成")
###########################################################
import csv # 向文件写入内容
def write_csv(file_path):
	with open(file_path,'w',newline='') as wstream:
		csv_write=csv.write(wstream)
		csv_write.writerow(['001','x',1])
		csv_write.writerow(['002','y',2])
		csv_write.writerow(['003','z',3])

file_path=r""
write_csv(file_path)
############################################################
import csv # 向文件写入内容(有标题)
def dictwrite_csv(file_path):
	with open(file_path,'w',newline='') as wstream:
		fieldnames=['sno','sname','age']
		csv_write=csv.DictWriter(wstream,fieldnames)
		csv_write.writeheader()
		csv_write.writerow({'sno':'001','sname':'x','age':1})
		csv_write.writerow({'sno':'002','sname':'y','age':2})
		csv_write.writerow({'sno':'003','sname':'z','age':3})

file_path=r""
dictwrite_csv(file_path)
############################################################
# 读取文件
def csv_reader():
	with open(file_path,'r',newline='') as rstream:
		csv_reader=csv.reader(rstream)
		for row in csv_reader:
			print(row)

# 读取文件
def csv_reader():
	with open(file_path,'r',newline='') as rstream:
		csv_reader=csv.DictReader(rstream)
		for row in csv_reader:
			print(dict(row))
############################################################
#文件备份
import os
import os.path
class FileBackup(object):
    def __init__(self, src, dist):
        """
        构造方法
        :param src: 目录 需要备份的文件目录
        :param dist: 目录 备份后的目录
        """
        self.src = src
        self.dist = dist

    def read_files(self):
        """
        读取src目录下的所有文件
        """
        ls = os.listdir(self.src)
        print(ls)
        for l in ls:
            # 循环处理每一个文件/文件夹
            # self.backup_file(l)
            self.backup_file2(l)
    def backup_file(self, file_name):
        """
        处理备份
        :param file_name: 文件/文件夹的名称
        """
        # 1. 判断dist是否存在，如果不存在，要创建这个目录
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print('指定的目录不存在，创建完成')
        # 2. 判断文件是否为我们要备份的文件
        # 拼接文件的完整路径
        full_src_path = os.path.join(self.src, file_name)
        full_dist_path = os.path.join(self.dist, file_name)

        # 首先要判断是否为文件夹，然后借助于文件的后缀名进行判断
        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == '.txt':
            print(full_src_path)
            # 3. 读取文件内容
            with open(full_dist_path, 'w', encoding='utf-8') as f_dist:
                print('>> 开始备份【{0}】'.format(file_name))
                with open(full_src_path, 'r', encoding='utf-8') as f_src:
                    while True:
                        rest = f_src.read(100)
                        if not rest:
                            break
                        # 4. 把读取到的内容写入到新的文件中
                        f_dist.write(rest)
                    f_dist.flush()
                print('>>> 【{0}】备份完成'.format(file_name))
        else:
            print('文件类型不符合备份要求，跳过>>')

    def backup_file2(self, file_name):
        """
        处理备份-优化版本
        :param file_name: 文件/文件夹的名称
        """
        # 1. 判断dist是否存在，如果不存在，要创建这个目录
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print('指定的目录不存在，创建完成')

        # 2. 判断文件是否为我们要备份的文件

        # 拼接文件的完整路径
        full_src_path = os.path.join(self.src, file_name)
        full_dist_path = os.path.join(self.dist, file_name)

        # 首先要判断是否为文件夹，然后借助于文件的后缀名进行判断
        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == '.txt':
            # 3. 读取文件内容
            with open(full_dist_path, 'w', encoding='utf-8') as f_dist, \
                open(full_src_path, 'r', encoding='utf-8') as f_src:
                print('>> 开始备份【{0}】'.format(file_name))
                while True:
                    rest = f_src.read(100)
                    if not rest:
                        break
                    # 4. 把读取到的内容写入到新的文件中
                    f_dist.write(rest)
                f_dist.flush()
                print('>>> 【{0}】备份完成'.format(file_name))
        else:
            print('文件类型不符合备份要求，跳过>>')

if __name__ == '__main__':
    # # 要备份的文件目录地址
    # src_path = 'C:\\Users\\yima1\\Desktop\\py_learn\\chapter04\\src'
    # # 备份后的目录地址
    # dist_path = 'C:\\Users\\yima1\\Desktop\\py_learn\\chapter04\\dist'

    # 当前代码的目录名称
    # C:\Users\yima1\Desktop\py_learn\chapter04\   test_backup.py
    base_path = os.path.dirname(os.path.abspath(__file__))
    # 要备份的文件目录地址
    src_path = os.path.join(base_path, 'src')
    print(src_path)
    # 备份后的目录地址
    dist_path = os.path.join(base_path, 'dist')
    print(dist_path)
    bak = FileBackup(src_path, dist_path)
    bak.read_files()



#####################################################################
序列化和反序列化
将对象可以通过网络传输或者可以存储到本地的数据格式的过程称为序列化，反之，
则称为反序列化,python实现序列化的方式有2种
1.json实现序列化和反序列化
import json
dict1={
	"k1":[
		{'sno':'001','sname':'a','age':1},
		{'sno':'002','sname':'b','age':2},
		{'sno':'003','sname':'c','age':3}
	],
	"k2":[
		{'sno':'004','sname':'x','age':4},
		{'sno':'005','sname':'y','age':5},
		{'sno':'006','sname':'z','age':6}
	]
}
result=json.dumps(dict1)
print(result)
print(type(result)) 	# <class 'str'>
# 反序列化
r=json.loads(result)
print(r)

students=r.get('k1')
for student in students:
	if "a" == student.get('sname'):
		print('找到了')
		break
else:
	print("没有找到")
############################################
with open("students.txt",'w') as wstream:
    json.dump(dict1,wstream)
print('保存成功')

with open("students.txt",'r') as rstream:
    content=json.load(rstream)
    print(content)
    students=content.get("k1")
    print(students)

2.pickle实现序列化和反序列化
import pickle
result=pickle.dumps(dict1)
print(result) 


r=pickle.loads(result)
print(r)

class Student:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def __str__(self):
		return self.name

stu=Student('xiaohua',2)
stu1=Student('ergou',3)
bobj=pickle.dumps(stu)
print(bobj)
stu=pickle.loads(bobj)
print(stu)

with open('stus.txt','wb') as ws:
	pickle.dump(stu,ws)
	pickle.dump(stu1,ws)

with open('stus.txt','rb') as rs:
	while True:
		try:
			content=pickle.load(rs)
			print(content)
		except :
			print('读取完毕')
			break


#########################################################
#用户数据保存和登录
class User(object):
	"""docstring for User"""
	def __init__(self):				
		self.username = None
		self.password=None
		self.status=None
		self.login_time=None

	def login(self,username,password):
		flag=True
		user_list=[]
		while True:
			try:
				user=pickle.load(rs)
				user_list.append(user)
				if user.username==username and user.password==password:
					if user.status:
						print("用户已经登录")
						self.login_time=login_time
						break
					else:
						print("登录成功")
						user.status=True
						self.login_time=datetime.now()
						flag=True
					self.username=username
					self.password=password
					self.status=status
			except:
				print("用户名或者密码不正确")
				break
		if flag:
			with open('user.txt','wb') as ws:
				for user in user_list:
					pickle.dump(user,ws)
	def logout():
		pass	

	def publish_comment(self):
		pass

	def register(self):
		pass

	def __str__(self):
		return self.username


def main():
	users={
		'u1':{"password":"123456","status":False,"login_time":"2022-08-21"},
		'u2':{"password":"123456","status":False,"login_time":"2022-08-22"},
		'u3':{"password":"123456","status":False,"login_time":"2022-08-23"}
	}
	user_obj=[]

	for key,value in users.items():
		u=User()
		u.username=key
		for k1,v1 in value.items():
			if k1=='password':
				u.password=v1
			elif k1=='status':
				u.status=v1
			elif k1=='login_time':
				u.login_time=v1
		user_obj.append(u)

	with open('users.txt','wb') as ws:
		for user in user_obj:
			pickle.dump(user,ws)

	print("保存成功")


if __name__ == '__main__':
	main()
	u=User()
	u.login('u1','123456')