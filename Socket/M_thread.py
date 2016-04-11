# import threading  # 导入threading包
# from time import sleep
# import time
#
#
# def task1():
#     print("Task 1 executed.")
#     sleep(1)
#
#
# def task2():
#     print("Task 2 executed.")
#     sleep(5)
#
#
# print("多线程：")
# starttime = time.time();  # 记录开始时间
# threads = []  # 创建一个线程列表，用于存放需要执行的子线程
# t1 = threading.Thread(target=task1)  # 创建第一个子线程，子线程的任务是调用task1函数，注意函数名后不能有（）
# threads.append(t1)  # 将这个子线程添加到线程列表中
# t2 = threading.Thread(target=task2)  # 创建第二个子线程
# threads.append(t2)  # 将这个子线程添加到线程列表中
#
# for t in threads:  # 遍历线程列表
#     t.setDaemon(True)  # 将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起
#     t.start()  # 启动子线程
# endtime = time.time();  # 记录程序结束时间
# totaltime = endtime - starttime;  # 计算程序执行耗时
# print("耗时：{0:.5f}秒".format(totaltime));  # 格式输出耗时
# print('---------------------------')
#
# # 以下为普通的单线程执行过程，不需解释
# print("单线程：")
# starttime = time.time();
# task1();
# task2();
# endtime = time.time();
# totaltime = endtime - starttime;
# print("耗时：{0:.5f}秒".format(totaltime));


# import time
# import threading
# exitFlag = 0
#
# class myThread (threading.Thread):   #继承父类threading.Thread
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
#         print("Starting " + self.name)
#         print_time(self.name, self.counter, 5)
#         print("Exiting " + self.name)
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threading.exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启线程
# thread1.start()
# thread2.start()
#
# print("Exiting Main Thread")

# 线程同步

import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print
        "Starting " + self.name
        # 获得锁，成功获得锁定后返回True
        # 可选的timeout参数不填时将一直阻塞直到获得锁定
        # 否则超时后将返回False
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print
        "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1


threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print
"Exiting Main Thread"
