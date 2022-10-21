"""timeit
测量小代码片段的执行时间

Timer:
	第一个参数是你要计算的语句或者函数，传递给Timer的第二个参数是为第一个参数语句
	构建环境的导入语句，从内部讲，timeit构建起一个独立的虚拟环境，手工的执行建立
	语句，然后手工的编译和执行被计时语句。一旦有了Timer对象，最简单是事就是调用
	timeit(),它接受一个参数为每个测试中调用被计时语句的次数，默认为一百万次；返回所
	耗时的秒数。
"""
from timeit import Timer
from timeit import timeit

def test():
	list1=[x for x in range(1,1000)]

t=Timer('test()','from __main__ import test')
# 生成列表消耗时间: 0.03503480000000003 秒
print('生成列表消耗时间:',t.timeit(1000),"秒") 

def del1():
	x=list(range(1000))
	for i in range(100):
		x.pop()


def del2():
	x=list(range(1000))
	for i in range(100):
		x.pop(0)

t1=timeit('del1()','from __main__ import del1', number=1000)
t2=timeit('del2()','from __main__ import del2', number=1000)
print('del1',t1,'秒') #del1 0.019722900000000015 秒
print('del2',t2,'秒') #del2 0.035301 秒


# 单链表
class Node:
    def __init__(self, date):
        self.date = date
        self.next = None

    def __str__(self):
        return str(self.date)


# 单链表构建一个list的结构
class SingleList:
    def __init__(self, node=None):
        self._head = node

    def isEmpty(self):
        return self._head == None

    def append(self, item):
        # 尾部添加
        node = Node(item)
        if self.isEmpty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def len(self):
        cur = self._head
        count = 0

        while cur != None:
            count += 1
            cur = cur.next
        return count

    def print_all(self):
        cur = self._head

        while cur != None:
            print(cur)
            cur = cur.next

    def pop(self, index):
        if index < 0 or index > self.len():
            raise IndexError('index error')
        if index == 0:
            self._head = self._head.next
        else:
            cur = self._head
            # 找到当前下标的前一个元素
            while index - 1:
                cur = cur.next
                index -= 1
            # 修改next的指向位置
            cur.next = cur.next.next

    def insert(self, index, item):
        if index < 0 or index > self.len():
            raise IndexError('index error')
        if isinstance(item, Node):
            raise TypeError('不是node类型')
        else:
            node = Node(item)

        if index == 0:
            node.next = self._head
            self._head = node
        else:
            cur = self._head
            while index - 1:
                cur = cur.next
                index -= 1
            node.next = cur.next
            cur.next = node

    def update(self, index, newitem):
        pass

    def remove(self, item):
        pass


if __name__ == '__main__':
    slist = SingleList()
    print(slist.isEmpty())
    print(slist.len())

    slist.append(5)
    print(slist.isEmpty())
    print(slist.len())

    slist.append(6)
    slist.append(7)

    slist.print_all()
    print('---------------------------------------')
    slist.pop(1)
    slist.print_all()

#############################################################
# 双向链表
class Node:
    def __init__(self, date):
        self.date = date
        self.next = None

    def __str__(self):
        return str(self.date)


class DoubleList:
    def __init__(self, node=None):
        self._head = node

    def isEmpty(self):
        return self._head is None

    def append(self, item):
        # 尾部添加
        node = Node(item)
        if self.isEmpty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    # 头部添加
    def add(self, item):
        node = Node(item)
        if self.isEmpty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def len(self):
        cur = self._head
        count = 0

        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def print_all(self):
        cur = self._head

        while cur is not None:
            print(cur)
            cur = cur.next

    def insert(self, index, item):
        if index < 0 or index > self.len():
            raise IndexError('index error')
        if index == 0:
            node = Node(item)
            node.next = self._head
            self._head.prev = node
            self._head = node
        else:
            node = Node(item)
            cur = self._head

            while index - 1:
                cur = cur.next
                index -= 1
            # cur就是index的前一个结点
            # 设置node节点的前一个是cur节点
            node.prev = cur
            # 设置node 的后一个节点
            node.next = cur.next
            # 设置cur的next节点就是node
            cur.next = node


    def remove(self, item):
        if self.isEmpty():
            raise ValueError('item not in double link list')
        else:
            cur = self._head
            if cur.date == item:
                # 删除头节点
                if cur.next is None:
                    self._head = None
                else:
                    # 除了头部节点还有其他节点
                    cur.next.prev = None
                    self._head = cur.next
            else:
                while cur is not None:
                    if cur.date == item:
                        cur.prev.next = cur.next
                        cur.next.prev = cur.prev
                        break
                    cur = cur.next

    def update(self, index, new_item):
        pass


if __name__ == '__main__':
    dlist = DoubleList()
    print(dlist.len())
    print(dlist.isEmpty())

    dlist.append(6)
    print(dlist.len())
    print(dlist.isEmpty())


##############################################
# 队列
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self, maxsize=-1):
        self.maxsize = maxsize  # 队列的容量
        self._head = None
        self._tail = None

    # 入队
    def enter(self, data):
        size = self.qsize()
        if self.maxsize != -1 and self.maxsize > size or self.maxsize == -1:
            node = Node(data)
            if self._head == None and self._tail == None:
                self._head = node
                self._tail = node
            else:
                self._tail.next = node
                self._tail = node
        else:
            raise Exception('queue is full')

    # 出队
    def exit(self):
        if self._head == None and self._tail == None:
            raise ValueError('queue is empty')
        data = self._head.data
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
        return data

    def print_all(self):
        cur = self._head
        while cur != None:
            print(cur)
            cur = cur.next

    def qsize(self):
        count = 0
        cur = self._head
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def isfull(self):
        pass

    def isEmpty(self):
        pass


if __name__ == '__main__':
    q = Queue()
    q.enter(1)
    q.enter(2)
    q.enter(3)

    q.print_all()
    print(q.qsize())

###########################################
#双端队列，可以在两端进行添加，删除操作，没有插入操作

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add_front(self, item):
        return self.items.insert(0, item)

    def add_rear(self, item):
        return self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_all(self):
        for item in self.items:
            print(item)


if __name__ == '__main__':
    dq = Deque()
    dq.add_front(1)
########################################################
#栈
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self,node=None):
        self.node=node
        self._head = None

    def push(self, item):  # 入栈
        node=Node(item)
        node.next=self._head
        self._head=node
        return node.data

    def pop(self):  # 弹栈
        if self._head==None:
            return None
        else:
            data=self._head.data
            self._head=self._head.next
            return data

    def peek(self):     # 出栈
        if self._head!=None:
            return  self._head.data
        else:
            raise ValueError('stack is empty')

    def print_all(self):
        cur=self._head
        while cur!=None:
            print(cur)
            cur=cur.next

if __name__ == '__main__':
    s=Stack()
    s.push(6)
    s.push(7)
    s.push(8)
    s.push(100)

    s.print_all()



############################################################
#树
class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur.lchild is None:
                cur.lchild = node
                return
            else:
                queue.append(cur.lchild)

            if cur.rchild == None:
                cur.rchild = node
                return
            else:
                queue.append(cur.rchild)

    # 广度优先遍历
    def breadth_tree(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            print(cur.data, sep=' ', end='')
            if cur.lchild is not None:
                queue.append(cur.lchild)
            if cur.rchild is not None:
                queue.append(cur.rchild)

    # 深度优先之先序遍历
    def front_travel(self, node):
        if node is None:
            return
        print(node.data, end='')
        self.front_travel(node.lchild)
        self.front_travel(node.rchild)

    # 深度优先之中序遍历
    def mid_travel(self, node):
        if node is None:
            return
        self.mid_travel(node.lchild)
        print(node.data, end=' ')
        self.mid_travel(node.rchild)

    # 深度优先之后序遍历
    def after_travel(self, node):
        if node is None:
            return
        self.after_travel(node.lchild)
        self.after_travel(node.rchild)
        print(node.data, end=' ')


if __name__ == '__main__':
    t = Tree()
    for i in range(10):
        t.add(i)
    t.breadth_tree()

    print('----------------------', end='\n')
    t.front_travel(t.root)

#######################################################################
import math
import random


def bubble_sort(l):  # 冒泡排序
    n = len(l)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


def duplex_bubble_sort(l):
    """
    自底向上,自顶向下交替进行双向扫描冒泡排序
    :param l: 要传入的列表
    :return: 无返回值
    """
    n = len(l)  # n表示列表的长度
    i = 0  # 设置列表的起始位置i=0
    flag = True  # 设置flag，判断列表元素是否有交换，初始值为True,表示有交换
    while flag:
        flag = False
        for j in range(n - i - 1, i, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
                flag = True  # 有交换

        for j in range(i + 1, n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                flag = True  # 有交换
        i = i + 1


def select_sort(l):  # 选择排序
    n = len(l)
    for i in range(n - 1):
        min_pos = i
        for j in range(i + 1, n):
            if l[j] < l[min_pos]:
                min_pos = j
        if min_pos != i:
            l[i], l[min_pos] = l[min_pos], l[i]


def insert_sort(l):  # 插入排序
    n = len(l)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]


def shell_insert_sort(l):  # 希尔排序
    n = len(l)
    gap = n // 2  # 步长

    while gap > 0:
        # 按照步长进行插入排序
        for i in range(gap, n):
            j = i
            while j >= gap and l[j - gap] > l[j]:
                l[j - gap], l[j] = l[j], l[j - gap]
                j -= gap

        gap = gap // 2

# 生成一个列表
list1 = [math.pow(i,2) for i in range(random.randint(0, 20))]  
random.shuffle(list1)  # 洗牌，打乱list1的列表顺序
print(len(list1))
print('排序前', list1)
# bubble_sort(list1)
# select_sort(list1)
# insert_sort(list1)
# duplex_bubble_sort(list1)
shell_insert_sort(list1)
print('排序后', list1)