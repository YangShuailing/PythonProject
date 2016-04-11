#coding=utf-8
# __author__ = yang
# print("hello world")

# 输入输出
# a=input("请输入a \n")
# print ("a=",a)

# 字符串
# s = 'ilovepython'
# print(s[0:5])
# print(s[-1:-7:-1]) # 反向取值

# list
# list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']
# print(list[2:])# 输出从第三个开始至列表末尾的所有元素
# print(tinylist*2)# 输出列表两次
# print(list+tinylist)# 打印组合的列表

# 元组
# tuple=('abcd',789,2.23,'john',70.2)
# tinytuple = (123,'john')
# print(tuple) # 输出完整元组
# print(tuple[0]) # 输出元组的第一个元素
# print(tuple[2:]) # 输出从第三个开始至列表末尾的所有元素
# print(tinytuple * 2) # 输出元组两次
# print(tuple + tinytuple) # 打印组合的元组
# print(tuple[1:3]) # 输出第二个至第三个的元素

# #  dictionary
# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
# tinydict = {'name':'john','num':'6734','class':'1414'}
# print(dict['one']) # 输出键为'one' 的值
# print(dict[2]) # 输出键为 2 的值
# print(tinydict) # 输出完整的字典
# print(tinydict.keys()) # 输出所有键
# print(tinydict.values()) # 输出所有值

# ## 算术运算符
# a = 21
# b = 10
# c = 0
# print('a=',a,'b=',b)
# c = a + b
# print("a + b 的值为：", c)
#
# c = a - b
# print("a - b 的值为：", c)
#
# c = a * b
# print("a * b 的值为：", c)
#
# c = a / b
# print("a / b 的值为：", c)
#
# c = a % b
# print("a % b 的值为：", c)
#
# # 修改变量 a 、b 、c
# a = 2
# b = 3
# print('a=',a,'b=',b)
# c = a**b
# print(a,'的',b,"次幂的值为：", c)
#
# a = 11
# b = 5
# print('a=',a,'b=',b)
# c = a//b
# print(a,'整除',b,"的值为：", c)

# # 例2：elif用法
# num = 5
# if num == 3:            # 判断num的值
#     print('boss')
# elif num == 2:
#     print('user')
# elif num == 1:
#     print('worker')
# elif num < 0:           # 值小于零时输出
#     print('error')
# else:
#     print('roadman')     # 条件均不成立时输出

## while
# count = 0
# while count < 9:
#    print('The count is:', count)
#    count = count + 1
#
# print("Good bye!")

# count = 0
# while count < 5:
#    print(count, " is  less than 5")
#    count = count + 1
# else:
#    print(count, " is not less than 5")

#  for用法
# fruit = ['banana','apple','mango']
# for index in range(len(fruit)):
#     print('当前水果',fruit[index])

# for num in range(10,20):
#     for i in range(2,num):
#         if num%i == 0:
#             j = num/i
#             print('%d 等于 %d*%d'%(num,i,j))
#             break
#     else:
#         print(num,'是一个质数')


# ### 循环嵌套
# i= 2
# while(i<100):
#     j=2
#     while(j<=(i/j)):
#         if not(i%j):
#             break
#         j = j + 1
#     if(j>i/j):
#         print(i,'是素数')
#     i = i + 1
# print('Good Bye')
#
#  # 字符串
# a = "Hello"
# b = "Python"
#
# print("a + b 输出结果：", a + b)
# print("a * 2 输出结果：", a * 2)
# print("a[1] 输出结果：", a[1])
# print("a[1:4] 输出结果：", a[1:4])
#
# if ("H" in a):
#     print("H 在变量 a 中")
# else:
#     print("H 不在变量 a 中")
# if ("M" not in a):
#     print("M 不在变量 a 中")
# else:
#     print("M 在变量 a 中")
# print(r'\n')
# print(R'\n')

# print("My name is %s and weight is %d kg!" % ('Zara', 21))

# 字典
# a = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# b = {'Name': 'Zara', 'Age': 7}
# print(type(a))
# del dict['Name'] # 删除键是'Name'的条目
# print(dict)
# dict.clear()     # 清空词典所有条目
# del dict         # 删除词典
# print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])

### 时间日期
# import time
#
# ticks = time.time()
# # print('当前时间戳：',ticks)
# # localtime = time.localtime(time.time())
# # print(localtime)
# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)
#
# import calendar
# print(calendar.firstweekday())
# print(calendar.calendar(2016))
# cal = calendar.month(2016,4)
# print("以下输出2016年四月的日历:")
# print(cal)

#  函数
# 定义函数
# def printme( str ):
#    print(str) # "打印任何传入的字符串"
#    return
#
# # 调用函数
# printme("我要调用用户自定义函数!")
# printme(str="再次调用同一函数")

## 不定长参数
# def printinfo(arg1,*vartuple):
#     # 打印任意长度
#     print("输出：")
#     print(arg1)
#     for i in vartuple:
#         print(i)
#     return
# print(10)
# print(10,11,12)

# # # 匿名函数 lambda
# sum = lambda arg1,arg2:arg1+arg2
# # 调用sum函数
# print("相加后的值为 : ", sum( 10, 20 ))
# print("相加后的值为 : ", sum( 20, 20 ))


###m 模块

# 导入内置math模块
# import math
# content = dir(math)
# print(content);
# ###自建模块 __init__
# import TecProject
# TecProject.leap()

## python i/o
# str = input("请输入：")
# print("你输入的内容是: ", str)

# 打开一个文件
# fo = open("foo.txt", "wb")
# print("文件名: ", fo.name)
# print("是否已关闭 : ", fo.closed)
# print("访问模式 : ", fo.mode)
## 读
# fo = open("foo.txt", "w+")
# fo.write("www.runoob.com!\nVery good site!\n")
# fo.close()
## 写
# fo = open("foo.txt", "r+")
# str = fo.read()
# str = fo.readline() #读取整行，包括 "\n" 字符
# position = fo.tell() # 查找当前位置
# fo.next() #返回文件下一行。
# print(str)
# print(position)
# fo.close()

import os
# 重命名文件test1.txt到test2.txt。
# fo = open("text1.txt","w")
# fo.close()
# os.rename("text1.txt","text2.txt")
# os.remove("text2.txt")
# os.mkdir("test") # 创建目录
# os.chdir("test") # 改变当前的目录
# fo = open("test.txt",'a+')
# os.rmdir("/tmp/test") # 删除”/tmp/test”目录
#
# ## 异常
# try:
#    fh = open("testfile.txt", "w")
#    fh.write("This is my test file for exception handling!!")
# except IOError:
#    print("Error: can\'t find file or read data")
# else:
#    print("Written content in the file successfully")
#    fh.close()

# ### 类
# class Employee:
# #empCount变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用Employee.empCount访问。
# # 第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
#    # '所有员工的基类'
#    empCount = 0
#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
#
#    def displayCount(self):
#      print("Total Employee %d" % Employee.empCount)
#
#    def displayEmployee(self):
#       print("Name : ", self.name,  ", Salary: ", self.salary )
#
#
# emp1 = Employee("Zara", 2000) #"创建 Employee 类的第一个对象"
# emp2 = Employee("Manni", 5000) #"创建 Employee 类的第二个对象"
# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee %d" % Employee.empCount)
#
# emp1.age = 7  # 添加一个 'age' 属性
# emp1.age = 8  # 修改 'age' 属性
# # del emp1.age  # 删除 'age' 属性
# print(hasattr(emp1, 'age'))    # 如果存在 'age' 属性返回 True。
# print(getattr(emp1, 'age'))   # 返回 'age' 属性的值
# print(setattr(emp1, 'age', 8)) # 添加属性 'age' 值为 8
# print(delattr(emp1, 'age'))    # 删除属性 'age'

# #  内部类
# class Employee:
#    '所有员工的基类'
#    empCount = 0
#
#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
#
#    def displayCount(self):
#      print("Total Employee %d" % Employee.empCount)
#
#    def displayEmployee(self):
#       print("Name : ", self.name,  ", Salary: ", self.salary)
#
# print("Employee.__doc__:", Employee.__doc__) # 类的文档字符串
# print("Employee.__name__:", Employee.__name__) # 类名
# print("Employee.__module__:", Employee.__module__) #  类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
# print("Employee.__bases__:", Employee.__bases__) # 类的所有父类构成元素（包含了以个由所有父类组成的元组）
# print("Employee.__dict__:", Employee.__dict__) # 类的属性（包含一个字典，由类的数据属性组成）


# ## 析构函数
#
# class Point:
#    def __init__( self, x=0, y=0):
#       self.x = x
#       self.y = y
#    def __del__(self):
#       class_name = self.__class__.__name__
#       print(class_name, "销毁")
#
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print(id(pt1), id(pt2), id(pt3)) # 打印对象的id
# del pt1
# del pt2
# del pt3

## 继承
# class Parent:        # 定义父类
#    parentAttr = 100
#    def __init__(self):
#       print "调用父类构造函数"
#
#    def parentMethod(self):
#       print '调用父类方法'
# ·
#    def setAttr(self, attr):
#       Parent.parentAttr = attr
#
#    def getAttr(self):
#       print "父类属性 :", Parent.parentAttr
#
# class Child(Parent): # 定义子类
#    def __init__(self):
#       print "调用子类构造方法"
#
#    def childMethod(self):
#       print '调用子类方法 child method'
#
# c = Child()          # 实例化子类
# c.childMethod()      # 调用子类的方法
# c.parentMethod()     # 调用父类方法
# c.setAttr(200)       # 再次调用父类的方法
# c.getAttr()          # 再次调用父类的方法


#### 正则表达式




