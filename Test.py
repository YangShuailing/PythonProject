# coding=utf-8
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

# 重命名文件test1.txt到test2.txt。
# fo = open("text1.txt","w")
# fo.close()
# os.rename("text1.txt","text2.txt")
# os.remove("text2.txt")
# os.mkdir("Socket") # 创建目录
# os.chdir("Socket") # 改变当前的目录
# fo = open("Socket.txt",'a+')
# os.rmdir("/tmp/Socket") # 删除”/tmp/Socket”目录
#
# ## 异常
# try:
#    fh = open("testfile.txt", "w")
#    fh.write("This is my Socket file for exception handling!!")
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

# # 继承
# class Parent:        # 定义父类
#    parentAttr = 100
#    def __init__(self):
#       print("调用父类构造函数")
#
#    def parentMethod(self):
#       print('调用父类方法')
#
#    def setAttr(self, attr):
#       Parent.parentAttr = attr
#
#    def getAttr(self):
#       print("父类属性 :", Parent.parentAttr)
#
# class Child(Parent): # 定义子类 class C(A, B):   # 继承类 A 和 B
#    def __init__(self):
#       print("调用子类构造方法")
#
#    def childMethod(self):
#       print('调用子类方法 child method')
# p = Parent
# c = Child()          # 实例化子类
# c.childMethod()      # 调用子类的方法
# c.parentMethod()     # 调用父类方法
# c.setAttr(200)       # 再次调用父类的方法
# c.getAttr()          # 再次调用父类的方法
# print(issubclass(Child,Parent)) #布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。

# ##  方法重写
'''
1  __init__ ( self [,args...] )
构造函数
简单的调用方法: obj = className(args)
2	__del__( self )
析构方法, 删除一个对象
简单的调用方法 : dell obj
3	__repr__( self )
转化为供解释器读取的形式
简单的调用方法 : repr(obj)
4	__str__( self )
用于将值转化为适于人阅读的形式
简单的调用方法 : str(obj)
5	__cmp__ ( self, x )
对象比较
简单的调用方法 : cmp(obj, x)
'''
#
# class Parent:  # 定义父类
#     def myMethod(self):
#         print('调用父类方法')
#
#
# class Child(Parent):  # 定义子类
#     def myMethod(self):
#         print('调用子类方法')
#
# c = Child()  # 子类实例
# c.myMethod()  # 子类调用重写方法
#  运算重载
# class Vector:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def __str__(self):
#         return 'Vector(%d,%d)' %(self.a,self.b)
#     def __add__(self, other):
#         return  Vector(self.a+other.a, self.b+other.b)
#
# v1 = Vector(1,2)
# v2 = Vector(3,4)
# print(v1 + v2)

# #  类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。
# 在类内部的方法中使用时 self.__private_attrs
#
# class PrivateVar:
#     __privateVar = 1  # 私有变量
#     publicVar = 1     # 公开变量
#
#     def  count(self):
#             self.__privateVar += 1
#             self.publicVar += 1
#             print(self.__privateVar)
#
#
# c = PrivateVar()
# c.count()
# print(c.publicVar)
# print(c.__privateVar) ## 报错

# 正则表达式

'''
模式字符串使用特殊的语法来表示一个正则表达式：
字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。
多数字母和数字前加一个反斜杠时会拥有不同的含义。
标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。
反斜杠本身需要使用反斜杠转义。
由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'/t'，等价于'//t')匹配相应的特殊字符。
下表列出了正则表达式模式语法中的特殊元素。如果你使用模式的同时提供了可选的标志参数，某些模式元素的含义会改变。

^	匹配字符串的开头
$	匹配字符串的末尾。
.	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
[...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
[^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
re*	匹配0个或多个的表达式。
re+	匹配1个或多个的表达式。
re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
re{ n}
re{ n,}	精确匹配n个前面表达式。
re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
a| b	匹配a或b
(re)	G匹配括号内的表达式，也表示一个组
(?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
(?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
(?: re)	类似 (...), 但是不表示一个组
(?imx: re)	在括号中使用i, m, 或 x 可选标志
(?-imx: re)	在括号中不使用i, m, 或 x 可选标志
(?#...)	注释.
(?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
(?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
(?> re)	匹配的独立模式，省去回溯。
\w	匹配字母数字
\W	匹配非字母数字
\s	匹配任意空白字符，等价于 [\t\n\r\f].
\S	匹配任意非空字符
\d	匹配任意数字，等价于 [0-9].
\D	匹配任意非数字
\A	匹配字符串开始
\Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。c
\z	匹配字符串结束
\G	匹配最后匹配完成的位置。
\b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n, \t, 等.	匹配一个换行符。匹配一个制表符。等
\1...\9	匹配第n个分组的子表达式。
\10	匹配第n个分组的子表达式，如果它经匹配。否则指的是八进制字符码的表达式。

[Pp]ython	匹配 "Python" 或 "python"
rub[ye]	匹配 "ruby" 或 "rube"
[aeiou]	匹配中括号内的任意一个字母
[0-9]	匹配任何数字。类似于 [0123456789]
[a-z]	匹配任何小写字母
[A-Z]	匹配任何大写字母
[a-zA-Z0-9]	匹配任何字母及数字
[^aeiou]	除了aeiou字母以外的所有字符
[^0-9]	匹配除了数字外的字符

.	匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
\d	匹配一个数字字符。等价于 [0-9]。
\D	匹配一个非数字字符。等价于 [^0-9]。
\s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
\S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
\w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
\W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。
'''

# 语法 re.match(pattern, string, flags=0)
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# import re
# # print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# # print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配
#
# import re
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

# import re
# line = "Cats are smarter than dogs"
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
#
# if matchObj:
#    print("matchObj.group() : ", matchObj.group())
#    print("matchObj.group(1) : ", matchObj.group(1))
#    print("matchObj.group(2) : ", matchObj.group(2))
# else:
#    print("No match!!")
#
#
# import re
# line = "Cats are smarter than dogs"
#
# searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
#
# if searchObj:
#    print("searchObj.group() : ", searchObj.group())
#    print("searchObj.group(1) : ", searchObj.group(1))
#    print("searchObj.group(2) : ", searchObj.group(2))
# else:
#    print("Nothing found!!")


# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。
# import re
#
# line = "Cats are smarter than dogs";
#
# matchObj = re.match( r'dogs', line, re.M|re.I)
# if matchObj:
#    print("match --> matchObj.group() : ", matchObj.group())
# else:
#    print("No match!!")
#
# matchObj = re.search( r'dogs', line, re.M|re.I)
# if matchObj:
#    print("search --> matchObj.group() : ", matchObj.group())
# else:
#    print("No match!!")

# ## re.sub用于替换字符串中的匹配项
# """
# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使 . 匹配包括换行在内的所有字符
# re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
#
# """
# import re
#
# phone = "2004-959-559 # This is Phone Number"
# # Delete Python-style comments
# num = re.sub(r'#.*$', "", phone)
# print("Phone Num : ", num)
# # Remove anything other than digits
# num = re.sub(r'\D', "", phone)
# print("Phone Num : ", num)

import random


def compareNum(num1, num2):
    if (num1 > num2):
        return 1
    elif (num1 == num2):
        return 0
    else:
        return -1


for i in range(1, 10):
    num1 = random.randrange(1, 9, 2)
    num2 = random.randrange(1, 9, 3)
    print("num1=", num1)
    print("num2=", num2)
    print(compareNum(num1, num2))
