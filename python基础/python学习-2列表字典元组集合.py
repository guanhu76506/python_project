
#列表(可变类型)及方法:
list1=[1,2,3,4,5,6,7,8,9,0]
#list(iterable)----> list()函数里面只能放可迭代的类型
list2=list("hello")     #['h', 'e', 'l', 'l', 'o']
list3=list1*2
#减少内存的拷贝，修改一个列表的数据时，避免使用list1 = list1 + list2这样的语法。
#list4=list1+list2 
#列表生成式
list5=[i * 10 for i in list1 if i % 2 ==0]
list5=[x+1 if i % 2 ==0 else x+2 for i in list1]    # 三目运算符应用于生成式
list6=[i*j for i in range(1,5) for j in range(1,5)]
max(list1) min(list1) sum(list1)
print(list1[-1],list1[1:4])
si=list1.index(4) # index函数用于获取指定元素的索引值,没有会报错
l=len(list1)  # len函数获取列表长度
#for循环遍历列表格式：  for 迭代变量 in 可迭代对象
for i in list1:
	print(i)
list1.reverse() # reverse()方法用于反转列表
list1.sort(reverse=True) #sort()方法用于排序,reverse=True代表降序排列
sorted(list1) #系统函数对列表进行排序
list1.append(11) 	#列表末尾追加元素
list1.insert(2,"x") #指定位置插入元素
list1.insert(len(list1),100)
list1[2]="二"    	#更新列表
list1.remove(2)  	#按照元素内容删除，没有找到删除元素会包ValueError
list1.pop(4)     	#按照索引位置删除元素，没有找到删除元素会包ValueError
list1[3:5]=[]    	#范围删除
list1.count(9)   	#统计出现的次数
list1.extend([666,888]) #将列表里的元素追加进去
p1=list1.copy()
p2=list1
print(p1 is list1) #False
print(p2 is list1) #True
del list1[3] #相当于pop(3)
del list1  #删除列表,删除地址
p2.clear() #清空列表,地址保存
# 随机产生qq号
qq=[]
count=0
while True:
    ran=random.randint(0,9)
    if count==0 and ran==0:
        continue
    qq.append(str(ran))
    count+=1
    if count=10:
        break
print(qq)
new_str=''.join(qq)     # join()函数必须要求所有元素都是字符串
print(new_str)

# 比较2个列表
flag=True
if len(list1)==len(list2):
    for i in range(0,len(list1))
        if list1[i]!=list2[i]
            flag=False
            break
    if not flag:
        print("不一样")
    else:
        print("一样")
else:
    print("不一样")

# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}\t".format(i,j,i*j),end="")
    print()

元组及常用内置函数：
t1=('a','b','c',1,2,3) #元组创建后内容不可变
print(t1[1:4],'b' in t1)
#如果元组内有列表，列表的内容是允许被修改的
t2=(['张三',38,5000],['李四'，28,2000])
item=t2[0]
item[1]=40
print(item,t2)
t3=t1+t2
t4=(10,)*3
print(t3,t4)
print(t1.index('c'),count(1))

系统方法：对元组排序：sorted(tuple) 排序返回的是列表
max(tuple),min(tuple),sum(tuple)


元组和列表使用到的符号是一样的
+ * [] [:] in is 
类型转换：
元组  ---->  列表: list(元组)
列表  ---->  元组: tuple(列表)


集合(可变类型)及其方法
无序的，不可重复的，底层实现是哈希表。不支持下标和切片
list1=[1,1,1,2,2,2,3,3,3]
set1=set(list1) #去重
college1={"哲学","经济学","法学"}
college2=set(["哲学","经济学","历史学"])
college3=set("中华人民共和国") # 使用set创建字符串集合
# 集合的方法
#intersection() 交集，获取两个集合中重复的部分  
c3=college1.intersection(college2)  # 相当于 c3=college1 & college2
# union() 并集，将两个集合所有元素合并去重
c4=college1.union(college2)     # 相当于 c4=college1 | college2
#difference() 差集, 两个集合之间差异的部分
c5=college1.difference(college2) # 相当于 c5=college1 - college2
#symmetric_difference() 双向差集
c6=college1.symmetric_difference(college2) # 相当于 c6=college1 ^ college2
print(c6)
college1.intersection_update(college2) #更新原有集合
print(college1)
college1.symmetric_difference_update(college2)
print(college1)
for c in college1: # 集合的遍历
    print(c)
print("计算机" in college1) #判断元素是否存在
college1.add("计算机") 
college1.update(college3) #一次添加多个元素，相当于列表方法extend()
college1.update("生物学","工程学")
college1.remove("生物") #remove如果删除不存在的元素时会报错
college1.pop()
college1.discard("生物") #discard如果删除不存在的元素时会忽略删除操作
college1.clear()  #清空集合
del college1

集合的关系操作：
s1={1,2,3}
s2={1,2,3,4,5,6}
print(s1==s2)
print(s1.issubset(s2)) #判断是否为子集
print(s2.issupperset(s1)) #判断是否为父级
print(s1.isdisjoint(s2))  #判断是否有重复元素

集合支持的符号： &(交集) |(并集) -(差集) ^(对称差集) in is
集合生成式：
set_x={i*j for i in range(1,4) for j in range(1,4) if i==j}

#字典(可变类型)及其方法
键值对保存，健不能重复，不能是列表类型，值是可以重复的
字典没有下标，因为底层实现是哈希表
dict1 = dict(name="李四", age=33, hiredate="2022-02-22")  # 创建字典方法1
dict2 = dict.fromkeys(["name", "age", "hiredate"], "N/A")  # 创建字典方法2
print(dict2)

employ = {"name": "张三", "age": 3, "hiredate": "2022-02-02"}  # 创建字典方法3
for e in employ:  # 遍历字典
    print(e)
for key, value in employ.items():
    print(key, value)
# 字典的获取方式1,如果key不存在的话，则报KeyError
name = employ["name"]  
# 字典的获取方式2,get(key[,default]),如果key不存在,且没有设置默认值，则返回None
#如果key不存在,且设置了默认值default，则返回default
print(employ.get("age"))
print(employ.get("age", 10))
print("name" not in employ)
print("dept" not in employ)

employ["name"] = "张三丰"  # 单个kv进行更新，有则更新，无则新增
employ.update(age=4, hiredate="2022-12-22")  # 多个kv进行更新
employ["dept"] = "技术部"  # 有则更新，无则新增
employ.update(weight=100, dept="研发部")  # 有则更新，无则新增

employ.pop("weight")  # 删除指定的kv
kv = employ.popitem()  # 从后往前删除一个kv

# setdefault()为字典设置默认值，如果某个key已存在则忽略，如果不存在则创建
dict2.setdefault("name", "xxx")
ks = dict2.keys()
print(ks, type(ks)) #dict_keys(['name', 'age', 'hiredate']) <class 'dict_keys'>

vs = dict2.values()
print(vs, type(vs)) #dict_values(['N/A', 'N/A', 'N/A']) <class 'dict_values'>

item = dict2.items()
#dict_items([('name', 'N/A'), ('age', 'N/A'), ('hiredate', 'N/A')]) <class 'dict_items'>
print(item, type(item))

dict2["hiredate"] = "2022-02-22"
# 利用字典格式化字符串
emp_str = "姓名:{name},年龄:{age},入职时间:{hiredate}".format_map(employ)
employ.clear()  # 清空字典
del dict1["key"] #根据key删除键值对，类似pop("key")
del dict1  #清空内容并回收内存

字典支持符号： in(可以使用，比较的是值) is


# 字典转列表：只能将字典中的key存放到列表里面
# 列表转字典：列表符合特定格式才能转换，否则无法转换  [("a":1),("b":2),("c":3)]


字典生成式：
list_x=["张三","李四","王五"]
dict_x={i+1:list_x[i] for i in range(0,len(list_x))}


