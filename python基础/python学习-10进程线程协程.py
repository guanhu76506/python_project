1、进程
import time
from multiprocessing import Process
def listen():
	musics=['两只老虎','两只蝴蝶','两只老鼠']
	for music in musics:
		print('在听歌:{}'.format(music))
		time.sleep(0.5)

def wechat(user):
	name='zheng'
	for i in range(5):
		print('{}在和{}聊天'.format(user,name))
		time.sleep(0.5)

def program():
	for i in range(10):
		print('在写代码第{}行'.format(i))
		time.sleep(0.5)


if __name__ == '__main__':
	p1=Process(target=listen)
	p2=Process(target=wechat,args=('zhangsan',))
	p3=Process(target=program)
	p1.start()
	p2.start()
	p3.start()

2、主进程和子进程
"""
一、
	主进程：执行的时候，默认的进程称作主进程
	子进程：在主进程中可以开启子进程
		p=Process(target=callable,args=(arg,))
二、全局变量
	如果是全局变量，则每个进程都会拥有一个全局变量。各自操作各自的全局变量
三、阻塞主进程
	子进程.join()
	阻塞主进程后面的代码
"""
def task1():
	for i in range(5):
		print('洗衣服:',i,os.getpid(),os.getppid())
		time.sleep(0.5)

def task2(n):
	for i in range(n):
		print('劳动最光荣，扫地中...',i,os.getpid(),os.getppid())
		time.sleep(0.5)

if __name__ == '__main__':
	p1=Process(target=task1)
	p2=Process(target=task2,args=(6,))
	p1.start()
	p2.start()
	print('main',os.getpid()) 

输出结果：
main 6540
洗衣服: 0 7212 6540
劳动最光荣，扫地中... 0 5384 6540
劳动最光荣，扫地中... 1 5384 6540
洗衣服: 1 7212 6540
劳动最光荣，扫地中... 2 5384 6540
洗衣服: 2 7212 6540
劳动最光荣，扫地中... 3 5384 6540
洗衣服: 3 7212 6540
劳动最光荣，扫地中... 4 5384 6540
洗衣服: 4 7212 6540
劳动最光荣，扫地中... 5 5384 6540

##########################################################
print('------>top', os.getpid())
number = 100
def task1():
    global number
    for i in range(5):
        print('洗衣服:', i, os.getpid(), os.getppid())
        time.sleep(0.5)
    number -= 10
    print('洗衣服:', number)

def task2(n):
    global number
    for i in range(n):
        print('劳动最光荣，扫地中...', i, os.getpid(), os.getppid())
        time.sleep(0.5)
    number -= 1
    print('扫地:', number)

if __name__ == '__main__':
    print('main---->start', os.getpid())
    p1 = Process(target=task1)
    p2 = Process(target=task2, args=(6,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('main---->end', os.getpid())
    print('main中的number是:', number)

输出结果：
------>top 5224
main---->start 5224
------>top 7608
洗衣服: 0 7608 5224
------>top 12616
劳动最光荣，扫地中... 0 12616 5224
洗衣服: 1 7608 5224
劳动最光荣，扫地中... 1 12616 5224
洗衣服: 2 7608 5224
劳动最光荣，扫地中... 2 12616 5224
洗衣服: 3 7608 5224
劳动最光荣，扫地中... 3 12616 5224
洗衣服: 4 7608 5224
劳动最光荣，扫地中... 4 12616 5224
洗衣服: 90
劳动最光荣，扫地中... 5 12616 5224
扫地: 99
main---->end 5224
main中的number是: 100

#################################################################
"""进程对象的方法
run() 		只运行不拥有资源
start() 	运行并分配资源
join()		阻塞进程
terminate() 中止进程
close()		进程释放资源
is_alive()	判断进程任务是否完成，如果任务完成则为false，没有完成结果为True
"""
def task1():
	for i in range(5):
		print('洗衣服:',i,os.getpid(),os.getppid())
		time.sleep(0.5)

def task2(n):
	for i in range(n):
		print('劳动最光荣，扫地中...',i,os.getpid(),os.getppid())
		time.sleep(0.5)

if __name__ == '__main__':
	p1 = Process(target=task1)
    p2 = Process(target=task2, args=(6,))
    p1.start()
    p2.start()
    for i in range(10):
        if i == 4:
            p1.terminate()

        elif i == 5:
            p2.terminate()

        time.sleep(0.5)
        print('main', i)
    p2.close()
    print('p1是否活着', p1.is_alive())
    print('p2是否活着', p2.is_alive())
##################################################################
#进程池
def task1():	
	print('洗衣服:',os.getpid(),os.getppid())
	time.sleep(0.5)
	return '我是进程'+str(os.getpid())
def callback(msg):
	print('{}洗衣任务完成！'.format(msg))

if __name__ == '__main__':
	pool=Pool(4)
	# 非阻塞式
	for i in range(10):
		pool.apply_async(task1,callback=callback)
	# 添加任务结束
	pool.close()
	# 阻塞主进程
	pool.join()

	print('main over')
输出结果：
洗衣服: 13164 10016
洗衣服: 2332 10016
洗衣服: 572 10016
洗衣服: 12776 10016
我是进程13164洗衣任务完成！
洗衣服: 13164 10016
我是进程2332洗衣任务完成！
洗衣服: 2332 10016
我是进程572洗衣任务完成！
洗衣服: 572 10016
我是进程12776洗衣任务完成！
洗衣服: 12776 10016
我是进程13164洗衣任务完成！
洗衣服: 13164 10016
我是进程2332洗衣任务完成！
洗衣服: 2332 10016
我是进程572洗衣任务完成！
我是进程12776洗衣任务完成！
我是进程13164洗衣任务完成！
我是进程2332洗衣任务完成！
main over

###################################################################
def task1():
    for i in range(2):
        print('洗衣服:', i, os.getpid(), os.getppid())
        time.sleep(0.5)
    return '我是进程' + str(os.getpid())


def callback(msg):
    print('{}洗衣任务完成！'.format(msg))


if __name__ == '__main__':
    pool = Pool(4)
    # 阻塞式
    for i in range(10):
        pool.apply(task1) #阻塞式:进程中的一个任务完成之后才能做下一个任务
        print("---------------------------------->",i)
    # 添加任务结束
    pool.close()
    # 阻塞主进程
    pool.join()

    print('main over')
输出结果：
洗衣服: 0 12496 11108
洗衣服: 1 12496 11108
----------------------------------> 0
洗衣服: 0 3864 11108
洗衣服: 1 3864 11108
----------------------------------> 1
洗衣服: 0 8000 11108
洗衣服: 1 8000 11108
----------------------------------> 2
洗衣服: 0 6916 11108
洗衣服: 1 6916 11108
----------------------------------> 3
洗衣服: 0 12496 11108
洗衣服: 1 12496 11108
----------------------------------> 4
洗衣服: 0 3864 11108
洗衣服: 1 3864 11108
----------------------------------> 5
洗衣服: 0 8000 11108
洗衣服: 1 8000 11108
----------------------------------> 6
洗衣服: 0 6916 11108
洗衣服: 1 6916 11108
----------------------------------> 7
洗衣服: 0 12496 11108
洗衣服: 1 12496 11108
----------------------------------> 8
洗衣服: 0 3864 11108
洗衣服: 1 3864 11108
----------------------------------> 9
main over

##################################################################
# 进程之间的通信--------------------------------->>>>>>>>>>>>>待验证实现
"""队列 from queue import Queue
	q=Queue(2) 
	q.put(1)
	q.put(2)
	print(q.full())
	q.get()
	print(q.qsize())
"""
from multiprocessing import Process, Pool
from queue import Queue
import requests
def download(urls, queue):
    for image_url in urls:
        response = requests.get(image_url)
        image_data = response.content
        queue.put(image_data)

def save_file(queue):
    while True:
    	try:
	    	count=0
	    	data=queue.get(timeout=5)
	    	# 保存到本地
	    	filename='img'+str(count)+'.jpg'
	    	with open('images/'+filename,'wb') as ws:
	    		ws.write(data)
	    	count+=1
	    	print('保存{}完毕'.format(filename))
	    except Exception as err:
	    	print('没有更多数据了')
	    	break
if __name__ == '__main__':
    
    q = Queue(2)
    images=[
        'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg10.360buyimg.com%2Fn0%2Fjfs%2Ft1%2F159004%2F1%2F9384%2F41770%2F603df390Ed3d1dbcc%2F167bc9275d6c7617.jpg&amp;refer=http%3A%2F%2Fimg10.360buyimg.com&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1662542728&amp;t=37b461b83b3d854c07ecb349d9e26836',
        'https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fq_70%2Cc_zoom%2Cw_640%2Fimages%2F20181218%2Fd7f9b5acf01344a39bd1ba1db1e6e283.jpeg&amp;refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1662542728&amp;t=30bb70dc3df829906bacf268e824894b'
    ]
    p1 = Process(target=download, args=(images, q))
    p2 = Process(target=save_file, args=(q,))
    start=time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end=time.time()
    print('共耗时{}秒'.format(end-start))
######################################################################
# 自定义进程
class ZDYProcess(Process):
	def __init__(self,urls,queue):
		Process.__init__(self)
		self.urls=urls
		self.queue=queue

	def run(self):
		for image_url in self.urls:
			filename=os.path.split(url)[1]
	        response = requests.get(image_url)
	        image_data = response.content
	        queue.put(image_data)
	        queue.get()
	        print('下载{}完毕'.format(filename))
	    self.queue.close()

if __name__ == '__main__':
	q1=Queue(2)
	images=[
        'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fimg10.360buyimg.com%2Fn0%2Fjfs%2Ft1%2F159004%2F1%2F9384%2F41770%2F603df390Ed3d1dbcc%2F167bc9275d6c7617.jpg&amp;refer=http%3A%2F%2Fimg10.360buyimg.com&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1662542728&amp;t=37b461b83b3d854c07ecb349d9e26836',
        'https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fq_70%2Cc_zoom%2Cw_640%2Fimages%2F20181218%2Fd7f9b5acf01344a39bd1ba1db1e6e283.jpeg&amp;refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=auto?sec=1662542728&amp;t=30bb70dc3df829906bacf268e824894b'
    ]
    dlprocess=Process(images,q1)
    dlprocess.start()

    for i in range(5):
    	if dlprocess.is_alive():
    		print('进程是活跃的',i)
    	else:
    		print('进程结束了')
    		dlprocess.close()
    		break
    	print('main',i)
    	time.sleep(1)

######################################################################
from threading import Thread

def task1():
	for i in range(5):
		print('洗衣服:',i,os.getpid(),os.getppid())
		time.sleep(0.5)

def task2(n):
	for i in range(n):
		print('劳动最光荣，扫地中...',i,os.getpid(),os.getppid())
		time.sleep(0.5)

if __name__ == '__main__':
	print('main',os.getpid())
	t1=Thread(target=task1)
	t2=Thread(target=task2,args=(6,))

	# 启动线程
	t1.start()
	t2.start()

	t1.join()
	t2.join()

	for i in range(3):
		print('t1:',t1.is_alive())
		print('t2:',t2.is_alive())
		print('main',i)
#输出结果：
main 7836
洗衣服: 0 7836 14144
劳动最光荣，扫地中... 0 7836 14144
洗衣服: 1 7836 14144
劳动最光荣，扫地中... 1 7836 14144
洗衣服: 2 7836 14144
劳动最光荣，扫地中... 2 7836 14144
洗衣服: 3 7836 14144
劳动最光荣，扫地中... 3 7836 14144
洗衣服: 4 7836 14144
劳动最光荣，扫地中... 4 7836 14144
劳动最光荣，扫地中... 5 7836 14144
t1: False
t2: False
main 0
t1: False
t2: False
main 1
t1: False
t2: False
main 2
######################################################################
# 自定义线程 必须重写run方法
class MyThread(Thread): 
	def __init__(self,name):
		Thread.__init__(self)
		self.name=name
	def run(self):
		for i in range(5):
			print('{}正在打印:{}'.format(self.name,i)) #默认的名字Thread1,Thread2...
			time.sleep(0.5)

if __name__ == '__main__':
	t1=MyThread('小花')
	t2=MyThread('小龙')
	t3=MyThread('小明')

	t1.start()
	t2.start()
	t3.start()
##################################################################
from threading import Thread,current_thread

def task1():
	for i in range(5):
		print('{}洗衣服:'.format(current_thread().name),i,os.getpid(),os.getppid())
		time.sleep(0.5)

def task2(n):
	for i in range(n):
		print('{}劳动最光荣，扫地中...'.format(current_thread().name),i,os.getpid(),os.getppid())
		time.sleep(0.5)

if __name__ == '__main__':
	print('main',os.getpid())
	t1=Thread(target=task1,name='警察')
	t2=Thread(target=task2,name='小偷',args=(6,))

	# 启动线程
	t1.start()
	t2.start()

	t1.join()
	t2.join()

##################################################################
#共享数据：如果是全局变量，则每个线程是共享的
from threading import Thread,current_thread
import time

ticket=10

def sale_ticket():
	global ticket
	while True:
		if ticket>0:
			print('{}正在卖第{}张火车票'.format(current_thread().name,ticket))
			ticket-=1
			time.sleep(0.5)
		else:
			break

if __name__ == '__main__':
	t1=Thread(target=sale_ticket,name='1号窗口')
	t2=Thread(target=sale_ticket,name='2号窗口')
	t3=Thread(target=sale_ticket,name='3号窗口')

	t1.start()
	t2.start()
	t3.start()

##################################################################
#GIL:针对python，一个线程拿到GIL锁，就拿到了CPU执行权，其它线程无法使用锁。
#直到该线程sleep，才会把GIL锁交出去
#缺点：虽然保证了数据的安全，但是效率降低了
number=0
def task():
	global number
	for i in range(1000000):
		number+=1

if __name__ == '__main__':
	t1=Thread(target=task,name='1号窗口')
	t2=Thread(target=task,name='2号窗口')
	t3=Thread(target=task,name='3号窗口')

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()

	print('number',number) # number 2206342
##################################################################

from threading import Thread, Lock
number = 0
def task(lock):
    global number
    lock.acquire() # 拿住锁
    for i in range(1000000):
        number += 1
    lock.release() #释放锁

if __name__ == '__main__':
    lock=Lock()
    
    t1 = Thread(target=task, name='1号窗口',args=(lock,))
    t2 = Thread(target=task, name='2号窗口',args=(lock,))
    t3 = Thread(target=task, name='3号窗口',args=(lock,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print('number', number)

#################################################################
# 保证线程卖票安全性
from threading import Thread,current_thread
import time

ticket=50

def sale_ticket(lock):
	global ticket
	while True:
		lock.acquire(0.8)
		if ticket>0:
			print('{}正在卖第{}张火车票'.format(current_thread().name,ticket))
			ticket-=1
			
			lock.release()
			time.sleep(0.5)
		else:
			print('票卖完了')
			lock.release()
			break
		

if __name__ == '__main__':
	lock=Lock()
	t1=Thread(target=sale_ticket,name='1号窗口',args=(lock,))
	t2=Thread(target=sale_ticket,name='2号窗口',args=(lock,))
	t3=Thread(target=sale_ticket,name='3号窗口',args=(lock,))
	t4=Thread(target=sale_ticket,name='4号窗口',args=(lock,))

	t1.start()
    t2.start()
    t3.start()
    t4.start()

#################################################################
# 线程之死锁：申请锁的顺序使用不当，尽量避免死锁的产生
# 避免死锁： 1、重构代码 2加参数timeout
def task1(lock1,lock2):
	if lock1.acquire():
		print('{}获取到lock1锁'.format(current_thread().name))
		for i in range(5):
			print('{}------->{}'.format(current_thread().name,i))
			time.sleep(0.01)
		if lock2.acquire(timeout=2):
			print('{}获取到lock1,lock2'.format(current_thread().name))
			lock2.release()

	lock1.release()


def task2(lock1,lock2):
	if lock2.acquire():
		print('{}获取到lock2锁'.format(current_thread().name))
		for i in range(5):
			print('{}------->{}'.format(current_thread().name,i))
			time.sleep(0.01)
		if lock1.acquire(timeout=2):
			print('{}获取到lock1,lock2'.format(current_thread().name))
			lock1.release()

	lock2.release()
if __name__ == '__main__':
	lock1=Lock()
	lock2=Lock()

	t1=Thread(target=task1,args=(lock1,lock2))
	t2=Thread(target=task1,args=(lock1,lock2))

	t1.start()
	t2.start()
#################################################################
# 线程之生产者和消费者
from threading import Thread,current_thread
import time

def produce(queue):
	print('{}开门啦'.format(current_thread().name))
	foods=['好烧肉','肉饼','馒头','土豆丝']
	for i in range(1,21):
		food=random.choice(foods)
		print('{}正在加工中。。。'.format(food))
		time.sleep(1)
		print('加工完成，可以上菜了')
		queue.put(food)
	queue.put(None)

def consumer(queue):
	print('{}来吃饭啦'.format(current_thread().name))
	while True:
		food=queue.get()
		if food:
			print('正在享用美食：',food)
			time.sleep(0.5)
		else:
			print('{}把饭吃完啦,走人'.format(current_thread().name))
			break

if __name__ == '__main__':
	queue=Queue(8)
	t1=Thread(target=produce,name='老家肉饼',args=(queue,))
	t2=Thread(target=consumer,name='小明',args=(queue,))

	t1.start()
	t2.start()


#################################################################
"""线程的信号量
信号量的实现方式：在内部有一个counter计数器，每当我们s.acquire()一次，计数器就减一处理
，每当s.release()一次,计数器就进行加一处理，当计数器为0的时候其它线程就处于等待的状态
，counter的值就是同一时间可以开启线程的个数
"""

def task(s):
	# s.acquire()
	with s:
		for i in range(5):
			print('{}扫地。。。{}'.format(current_thread().name,i))
			time.sleep(i)
	# s.release()

if __name__ == '__main__':
	s=Semaphore(4)
	for i in range(10):
		t=Thread(target=task,args=(s,))
		t.start()


#################################################################
# 协程   微线程
def eat():
	for i in range(5):
		print('kk喜欢吃肉饼')
		yield

def listen_music():
	for i in range(5):
		print('kk喜欢听音乐',i)
		yield

if __name__ == '__main__':
	g1=eat()
	g2=listen_music()

	while True:
		try:
			next(g1)
			next(g2)
		except:
			break

#################################################################
#greenlet和gevent
from greenlet import greenlet
def eat():
	for i in range(5):
		print('kk喜欢吃肉饼')
		g2.switch()
		

def listen_music():
	for i in range(5):
		print('kk喜欢听音乐',i)
		g1.switch()
	
if __name__ == '__main__':
	g1=greenlet(eat)
	g2=greenlet(listen_music)	

	g1.switch()


#################################################################
from greenlet import greenlet
from gevent import monkey
import gevent
import time

monkey.patch_all()
def eat():
	for i in range(5):
		print('kk喜欢吃肉饼')
		time.sleep(0.2)
		

def listen_music():
	for i in range(5):
		print('kk喜欢听音乐',i)
		time.sleep(0.2)


if __name__ == '__main__':
	g1=gevent.spawn(eat)
	g2=gevent.spawn(listen_music)

	g1.join()
	g2.join()

	print('-----over-----')