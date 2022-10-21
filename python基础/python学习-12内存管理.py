

def extend_list(val, l=[]):
    l.append(val)
    print(l, id(l))
    return l
list1 = extend_list(10) 		# [10] 2086816880320
list2 = extend_list(123, [])	# [123] 2086816790336
list3 = extend_list('a')		# [10, 'a'] 2086816880320
print("===========")
print(list1)  	# [10, 'a']
print(list2)	# [123]
print(list3)	# [10, 'a']
解释：当extendList被没有指定特定参数list调用时，这组list的值随后将被使用。
这是因为带有默认参数的表达式在函数被定义的时候被计算，不是在调用的时候被计算。
因此list1和list3是在同一个默认列表上进行操作（计算）的。
而list2是在一个分离的列表上进行操作（计算）的。
（通过传递一个自有的空列表作为列表参数的数值）。

############################################################################

"""垃圾回收机制：
以引用计数为主，标记清除和分代收集为辅。一个对象的引用数为0，python虚拟机回收这个对象的内存。
引用计数的缺陷是循环引用的问题。每个对象都有存有指向该对象的引用总数。
python里的每一个东西都是对象，他们的核心就是一个结构体：PyObject

查看某个对象的引用计数：sys.getrefcount()
使用del关键字删除某个引用

循环引用的缺点：1、消耗计算机资源 2、所占用的资源无法被回收，导致内存泄漏。
GC系统所承担的工作远比"垃圾回收"多得多。实际上，它们负责三个重要的任务：
1、为新生成的对象分配内存
2、识别垃圾对象
3、从垃圾对象里回收内存
"""
import sys
l=[]
l2=l
l3=l
del l2
print(sys.getrefcount(l))  #3
l5=l3
i=0
print(sys.getrefcount(i))  #2224
m=i
print(sys.getrefcount(l))  #4
print(sys.getrefcount(i))  #2225
#########################################################
"""
当python运行时，会记录其中分配对象（object allocation）和
取消分配对象（object deallocation）的次数。当两者的差值高于
某个阈值时，垃圾回收才会启动。
查看阈值：gc.get_threshold()
Python将所有的对象分为0,1,2三代，所有的新建对象都是0代对象。
当某一代对象经历过垃圾回收，依然存活，那么它就被归入下一代对象。
手动回收：gc.collect()
objgraph模块中的count()记录当前类产生的实例对象的个数
"""
import gc,sys
print(gc.get_threshold())
class Persion():
   pass
class Cat():
   pass

p=Persion()
c=Cat()
p.name='zhangsan'
p.pet=c
c.master=p
print(sys.getrefcount(p))
print(sys.getrefcount(c))
#输出结果
(700,10,10)
3
3

##############################################################
内存池（memory pool）机制：
当创建大量消耗小内存对象时，频繁调用new/malloc会导致大量的内存碎片，
导致效率降低。内存池的概念就是预先在内存中申请一定数量的，大小相等的
内存块留作备用。当有新的内存需求时，就从内存池中分配内存给这个需求，
不够了之后再申请新的内存。这样就能减少内存碎片，提升效率。
Python3的内存管理机制——Pymalloc
针对小对象（<=512bytes），pymalloc会在内存池中申请内存空间。
当>512bytes，则会PyMem_RawMalloc()和PyMem_RawRealloc()来
申请新的内存空间。








list执行append()操作时,Python将一次拓展N个元素的内存，因为一个append操作很
可能是很多append操作的开始，通过额外分配内存来减少可能的内存分配和内存copy的次数。
import sys
l = []
#以f开头表示在字符串内支持大括号内的python表达式
print(f'list initial size {sys.getsizeof(l)}') #list initial size 56
for i in range(80):
   cur_size = sys.getsizeof(l)
   l.append(i)
   new_size = sys.getsizeof(l)
   print(f'list len {i+1}:\t current_size {new_size}\t new_allocated 8 * {(new_size-cur_size)/8}')
观察发现,列表从0增加到80长度的过程中,新申请的内存长度为[4,4,8,9,10,11,12,14,16] 
反之， 当执行remove或者pop减少列表中的数据时，列表也会自动缩容。
扩容条件 ，新长度大于底层数组长度；
缩容条件 ，新长度小于底层数组长度的一半；
结论： 避免使用类似append语法初始化列表，优先使用列表表达式