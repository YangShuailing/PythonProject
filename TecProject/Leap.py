#-*- coding:utf-8 -*-
def  leap(year):
 try:
    year = int(input('请输入年份(如2008):\n'))
 except:
    print ('请输入正确的年份')
 # exit()

 if (year%4== 0 and(year%100 != 0 or year%400 == 0)):
    print ('%d年是闰年！' % year)
 else:
    print ('%d年不是闰年！' % year)
 return

