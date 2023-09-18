# print("hello world")
# print("hello 'A'")
# print('hello "jack"')
# print("'hello "
#       "world "
#       "你好'")
# print("what is your name?")
# input()
# print("oh hello")
# input("please input your name")
# input("please input your name\n")
# name = "mayi"
# number = 123
# print(name)
# print(number)
# 全局变量：全大写_分隔 PHONE_NUMBER = "123"
# 普通变量：全小写，驼峰命名法 phoneNumber = "123"
# 实例变量（类属性变量）：以_开头 _phoneNumber
# 私有实例变量（外部访问会报错）：以双下划线__开头 __phoneNumber
# 专有变量：__开头__结尾 __init__
# print("what is your name")
# name = input()
# print("hi!" + name)
# print("how old are you")
# age = input()
# print("when were you born?:"+str(2017-int(age)))
# age = 20
# print("your age is :" + str(age))
# my_num = 45
# converted_my_num = str(my_num)
# print("123",int(converted_my_num)+11)
# print("how old are you?")
# age = input()
# print("your age is:%s" % age)
# print("what is your name?")
# name = input()
# print("how old are you?")
# age = int(input())
# print("your name is %s,your age is %d"%(name,age))
# print("what is your name?")
# name = input()
# print("how old are you?")
# age = int(input())
# print("my name is %s,I am %d year old" %(name,age))
# print("my name os %s,I am %d year old."%("zhansan",20))
# print("%d+%d=%d"%(2,3,2+3))
# print("the book is $%f"%20.00)
# print("%+10d"%123)
# print("%+10d"%-123)
# print("%d"%-123)
# # print("%-10d"%123)
# # print("%010d"%123)
# print("%*.*f"%(6,2,12.345))
# print("my name is %(name)s."%{"name":"zhangsan"})
# abc = 10
# print("please  enter a number:")
# num = int(input())
# result = num>abc
# print("太大了  "+str(result))
# # print(result)
# result = num<abc
# print("太小了  "+str(result))
# # print(result)
# result = num==abc
# print("正确！  "+str(result))
# # print(result)
# abc = 10
# print("please enter a number:")
# num = int(input())
# if num>abc:
#     print("toobig")
# if num<abc:
#     print("toosmall")
# if num==abc:
#     print("right")
# abc = 10
# print("please enter a number")
# num = int(input())
# if num==abc:
#     print("right")
# elif num>abc:
#     print("toobig")
# else:
# #     print("toosmall")
# print("please enter a number")
# num = int(input())
# if num>=0:
#     if num<=20:
#         print("[0.20]")
#     else:
#         print(">20")
# else:
#     if num>-10:
#         print("(-10,0)")
#     else:
#         print("<=-10")
# abc = 10
# marks = True
# while marks:
#     print("please inter a number:")
#     num = int(input())
#     if num>abc:
#         print("toobig")
#     if num<abc:
#         print("toosmall")
#     if num==abc:
#         print("right")
#     marks = False
# for i in range(1,10):
#     print(i)
# for letter in "python":
#     if letter=="h":
#         break
# #     print("current letter:",letter)
# for letter in"python":
#     if letter=="h":
#         continue
#     print("current letter:",letter)
# def sayhello():
#     print("hello world!")
#
#
# sayhello()
# def print_max(a,b):
#     if a>b:
#         print(a)
#     else:
#         print(b)
# print_max(3,5)
# print_max(8,6)
# print_max(2,2)
# x = 10
# def print_x():
#     x = 5
#     print(x)
# print_x()
# print(x)
# print_x()
# x=10
# def print_x():
#     global x
#     x=5
#     print(x)
# print_x()
# print(x)
# x=10
# y=20
# def print_x():
#     global x
#     x=5
#     print(x)
#     print(y)
# print_x()
# print(x,y)
# def say_message(message,times):
#     print(message*times)
# say_message("hello",3)
# say_message("look",3)
# def print_abc(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# print_abc(1,2,3)
# print_abc(c=3,b=2,a=1)
# def maxnum(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# print(maxnum(3,5))
# a=maxnum(9,5)
# print(a)
# from random import randint
# def compare(x,y):
#     if x==y:
#         print("bingo!")
#         return True
#     elif x<y:
#         print("toosmall")
#         return False
#     elif x>y:
#         print("toobig")
#         return False
# num=randint(1,100)
# bingo=False
# while(bingo==False):
#     print("please guess")
#     answer=int(input())
#     bingo=compare(answer,num)
# from random import randint
# num=randint(1,100)
# print(num)
# import random
# num=random.randint(1,100)
# print(num)
# from random import randint as ra
# import random
# num=ra(1,100)
# print(num)
# print(ra(1,100))
# print(dir(random))
# list1 = ['physics','chemistry',1997,2000]
# list2 = [1,2,3,4,5,6,7]
# print("list1[0]:",list1[0])
# print("list2[1:5]",list2[1:5])
# list = ['physics','chemistry',1997,2000]
# print("Value available at index2:")
# print(list[2])
# list[2]=2001
# print("New value available at index2:")
# print(list[2])
# print(list)
# l1=[1,2,3,4,5]
# l2=[1,'a',2,'b',11]
# print(l1)
# print(l2)
# tup1=('physics','chemistry',1997,2000)
# tup2=(1,2,3,4,5,6,7)
# print('tup1[0]:',tup1[0])
# print('tup2[1:5]',tup2[1:5])
# tup1=(12,34.56)
# tup2=('abc','xyz')
# tup3=tup1+tup2
# print(tup3)
# a=(1)
# t1=(1,)
# t2=()
# print(a)
# print(t1)
# print(t2)
# dict1={'abc':456}
# dict2={'abc':123,98.6:37}
# print(dict1,dict2)
# print(dict2[98.6])
# dict={'name':'zara','age':7,'class':'first'}
# print('dict["name"]:',dict["name"])
# print('dict["age"]:',dict['age'])
# dict={'name':'zara','age':7,'class':'first'}
# print(dict)
# dict={'name':'zara','age':7,'class':'first'}
# dict['age']=8
# dict['name']='zhangsan'
# dict['school']='dps school'
# print('dict["age"]',dict['age'])
# print('dict["school"]',dict['school'])
# t1=(1,2,3,4,5)
# l1=[1,2,3,4,5]
# d1={'a':1,'b':2,'c':3}
# print(l1[0],l1[1],t1[0],t1[1],d1['a'],d1['b'])
# print(l1[-1],l1[-2],t1[-1],t1[-2])
# print(l1[0:2],l1[0:],l1[:2],l1[:],l1[0:-2])
# for i in l1:
#     print(i)
# print('over')
# for j in t1:
#     print(j)
# for k in d1:
#     print(k)
# t1=(1,2,3,4,5)
# l1=[1,2,3,4,5]
# d1={'a':1,'b':2,'c':3}
# l1.append(6)
# d1['d']=4
# print(l1,d1)
# del l1[0]
# del d1['a']
# print(l1,d1)
# range(1,5)
# print(range(1,5))
# for i in range(1,5):
#     print(i)
# str1='my name is Tom'
# l1=str1.split()
# print(l1,l1[0],l1[1])
# tup1=(1,2,3,4,5)
# tup1.append(6)
# del tup1(0)
# l1=['my','name','is','Tom']
# s1=' '
# print(s1.join(l1))
# s2='.'
# print(s2.join(l1))
# str1='my name is Tom'
# for i in str1:
#     print(i)
# print(str1[0],str1[1],str1[0:5])
# str1[0]=h  #不能用索引去改变字符串中的字符
# print(str1)
# with open("1.txt","a+") as filewrite:
#     filewrite.write('\nI like you know')
# with open('C:/Users/24512/Desktop/1.txt','a') as filewrite:
#     filewrite.write('\nI like java')
# with open('C:/Users/24512/Desktop/1.txt') as fileopen:
#     # config_data=fileopen.read()
#     # print(config_data)
#     config_data=fileopen.readline()
#     print(config_data)
# try:
#     print('please enter a number:')
#     num=int(input())
#     if num>0:
#         print('yes')
#     else:
#         print('no')
# except:
#     print('Failed')
#     print('you must enter a number.')
# try:
#     n=5*6
#     print('n=',n)
#     v=5+a
#     print('v=',v)
#     m=5/0
#     print('m=',m)
# except ZeroDivisionError:
#     print('发生0为除数的异常')
# except:
#     print('其它异常')
# print('计算完成')
# try:
#     with open('abc.txt','r') as f:
#         config_data=f.read()
#         print(config_data)
#         f.close()
# except(IOError,TypeError,ValueError):
#     print('the file is not exist')
# try:
#     with open('C:/Users/24512/Desktop/1.txt','r') as f:
#         config_data=f.read()
#         print(config_data)
#         f.close()
# except IOError:
#     print('the fail is not exist')
# except TypeError:
#     print('tpye is wrong')
# except ValueError:
#     print('value is wrong')
# else:
#     print('there is no exception')
# finally:
#     print('bye')
# class Employee:
#     __empCount = 0
#     def __init__(self,myName,mySalary):
#         self.name = myName
#         self.salary = mySalary
#         Employee.__empCount += 1
#
#     def displayCount(self):
#         print('Total Employee %d' % Employee.__empCount)
#
#     def displayEmployee(self):
#         print('Name:', self.name, 'Salary:', self.salary)
#
# emp1 = Employee('zhangsan', 2000)
# emp1.displayEmployee()
# emp1.displayCount()
# emp2 = Employee('lisi',5000)
# emp2.displayEmployee()
# emp2.displayCount()
# # print('Total Employee %d'%Employee.__empCount)
# class Animal:
#     def eat(self):
#         print('eat')
#     def sleep(self):
#         print('sleep')
# class Bnimal(Animal):
#     def move(self):
#         print('move')
#     def eat(self):
#         print('noeat')
#
# b1 = Bnimal()
# Animal().eat()
# b1.eat()
# b1.sleep()
# b1.move()
# import json
# import sys
#
# f = open('1.txt','r')
# print(f.read(10))
# f.close()
#
# import urllib
# def report(a,b,c):
#     per=100.0*a*b/c
#     if per>100:
#         per=100
#         print('%.2f%%'%per)
# report(9,2,3)
# from urllib import request
# request.urlretrieve('https://blog.csdn.net/qq_27524749',
#                     'C:/Users/24512/Desktop/csdn.html')
# from urllib import request as urllib2
# f = urllib2.urlopen('http://www.weather.com.cn/adat/cityinfo/101270101.html')
# config_data = f.read()
# # print(config_data)
# # f.close()
# from json import loads
# d = loads(config_data)
# d1 = d['weatherinfo']
# print('城市：',d1['city'],'最低温度：',d1['temp2'],'最高温度：',d1['temp1'])
# f.close()
#
# import socket
# import time
# s_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s_client.connect(('localhost',9001))
# time.sleep(3)
# s_client.send('1'.encode(encoding='utf_8', errors='strict'))
# print(s_client.recv(1024))
# s_client.close()
#
# s_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s_server.bind(('localhost',9001))
# s_server.listen(5)
# while True:
#     connection,address=s_server.accept()
#     try:
#         connection.settimeout(5)
#         message = connection.recv(1024)
#         if message=='1':
#             connection.send('welcome to server!')
#         else:
#             connection.send('please go out!')
#     except socket.timeout:
#         print('time out')
#     connection.close()
#
# import MySQLdb
# conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='police_db',port=3306)
# cur = conn.cursor()
# count = cur.execute('select * from usertbl')
# print(count)
# result = cur.fetchone()
# print('id:%s,username:%s,password:%s'%result)
# cur.close()
# conn.close()
# import MySQLdb
# conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='test',port=3306)
# cur = conn.cursor()
# cur.execute('delete from user')
# cur.execute('insert into user values(1,"zhangsan1")')
# cur.execute("insert into user values(%d,'%s')"%(2,"zhangsan2"))
# sql_1 = []
# for i in range(3,11):
#     sql_1.append((i,'zhangsan'+str(i)))
#     sql_2=sql_1[i-3]
#     # print(sql_2)
#     cur.execute('insert into user values(%d,"%s")'%sql_2)
# count = cur.execute('select * from user')
# print(count)
# # result = cur.fetchone()
# # print('ID:%d,Name:%s'%result)
# # result1 = cur.fetchmany(5)
# # for re1 in result1:
# #     print('ID:%d,Name:%s'%re1)
# result2 = cur.fetchall()
# print(result2)
# for re2 in result2:
#     print('ID:%s,Name:%s'%re2)
# conn.commit()
# cur.close()
# conn.close()
#
# import re
# text = 'Hi,I am Shirly Hilton.'
# # m = re.findall('hi',text)
# m = re.match('Hi,I am Shirly Hilt',text)
# if m:
#     print(m)
#     print(m.group(0))
# else:
#     print('not maych')
#
# import re
# text = 'Hi,I am Shirly Hiton.'
# m = re.match(r'(Hi)(,)(I) (am) (Shirly) (Hiton)',text)
# if m:
#     print(m.group())
#     print(m.group(0))
#     print(m.group(1))
#     print(m.group(2))
#     print(m.group(3))
#     print(m.group(4))
#     print(m.group(5))
# else:
#     print('not match')
#
# import re
# text = 'Hi,I am Shirly Hiton.'
# m = re.match('Hi',text)
# if m:
#     print(m.start())
#     print(m.end())
# else:
#     print('not match')
# m = re.search('hi',text)
# if m:
#     print(m.group())
# else:
#     print('not match')
#
# import sys
# print('script name is',sys.argv)
# if len(sys.argv)>0:
#     # print('There are',len(sys.argv),'arguments:')
#     for arg in sys.argv[:]:
#         print(arg)
# else:
#     print('There are no arguments!')
# print(sys.path)
# print(sys.version)
# print(sys.platform)
# print(sys.exit())
# print(sys.getdefaultencoding())
# print(sys.getfilesystemencoding())
# import os
# print(os.name)
# print(os.getcwd())
# print(os.getenv('path'))  # os.putenv()
# print(os.listdir())
# os.remove("1.txt")
# import math
# print(math.e)
# print(math.pi)
# print(math.hypot(3.0,4.0))
# import copy
# a = [[1],[2],[3]]
# b = copy.copy(a)
# c = copy.deepcopy(a)
# print(a)
# print(b)
# print(c)
# a[1] = 0
# a[0][0] = 0
# print('-----------')
# # b = copy.copy(a)
# # c = copy.deepcopy(a)
# print(a)
# print(b)
# print(c)
# import string
# text = 'hello world'
# print(text.upper())
# print(text.lower())
# print(text.split())
# a = text.split()
# print("+".join(a))
# print(text.replace('hello','hi'))
# print(text.count('l'))
# import time
# now = time.time()
# print(now)
# print(time.gmtime(0))
# print(time.gmtime())
# print(time.localtime())
# print(time.asctime(time.localtime()))
# print(time.strftime('%y/%m/%d %H:%M',time.localtime()))
# import types
# var = 1
# print(type(var))
# print()
# help(print())
#
# num = 1
# num1 = int(input('请输入一个数字：'))
# if num1 > num:
#     print(f'{num1}大于{num}')
# elif num1<num:
#     print(f'{num1}小于{num}')
# else:
#     print(f'{num1}等于{num}')
#
# for i in range(5):
#     for j in range(i+1):
#         print('*',end=" ")
#     print()
# def add(num1,num2,num3=3):
#     return num1,num2,num3
# print(add(1,2))
#     # print(num1,num2,num3)
# add(1,2)
# # add(1,2,4)
# list = ['a','b','c','d','e','f']
# # print(list[-1:-4:-1])
# print(type(list))
# dict = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4','key5':'value5'}
# for i in dict:
#     print(f'{i}:{dict[i]}')
# print(len(dict))
# print(dict['key5'])
# # del dict['key5']
# dict.pop('key5')
# print(dict)
# tup = ('a','b','c','d','e')
# for i in tup:
#     print(i,end=' ')
# str = 'a#b#c#d#e'
# list = str.split("#")
# print(list)
# str1 = '$'.join(list)
# print(str1)
# a = [1,2,3]
# b = a
# c = a[::]
# a = [4,5,6]
# print(a,b,c)
# print(a)
# print(b)
# print(c)
#
# print(r'n\s\ns')
# with open(r'C:\Users\24512\Desktop\1.txt','r+') as file:
#     print(file.read())
#     file.close()
# print('a')
# help(print('a'))
#
# 简易购物系统
# 在系统中存在用户的id和账户余额，用户可以选择充值和购物，查询购买记录
# 1. 选择充值，会在用户的余额中增加对应的金额(充值不能为负)
# 2.选择购物，弹出对应的购物列表
#  每条用如下形式展示
#  商品id
#  商品名称
#  金额
#  让用户根据序号选择商品，加入购物车购买，如果商品总额大于总资产，提示账户余  额不足
# (一次只能购买一个商品  ps.选择实现 一次可以购物一个或者多个商品)
# 否则，购买成功。
# 3.查询所有的购买记录，显示订单号，购物的商品记录和总金额，如果没有买过任何商品，提示没有购买记录
#
# user     id  balance          deposit   shopping   query
# goods    id  name  amount
# {userId:xxx, goodsRecordList:goodsList, totalAmount: totalAmount}
# goodsRecords = []
#
#
# class Goods:
#     def __init__(self, goodsId, goodsName, amount):
#         self.goodsId = goodsId
#         self.goodsName = goodsName
#         self.amount = amount
#
#
# class User:
#     def __init__(self, userId, balance):
#         self.userId = userId
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount <= 0:
#             return "充值金额不能小于等于0，请重新填写！"
#         self.balance += amount
#         return f"充值成功！当前余额为{self.balance}"
#
#     def shopping(self, shopList):
#         # 购物车shopList = [apple, pear, banana, apple]
#         # 先计算购物车的总金额，判断余额是否足够
#         totalAmount = 0
#         shopList1 = []
#         for goods in shopList:
#             totalAmount += goods.amount
#             shopList1.append(goods.goodsName)
#         if self.balance < totalAmount:
#             return f"余额：{self.balance},商品总金额：{totalAmount},余额不足，请充值！"
#         # 用户余额减去购买的商品的总金额
#         self.balance -= totalAmount
#         # {userId: xxx, goodsRecordList: shopList, totalAmount: totalAmount}
#         dict = {"用户Id": self.userId, "购买商品列表": shopList1, "商品总金额": totalAmount}
#         goodsRecords.append(dict)
#         return f"购买成功！当前余额为{self.balance}"
#
#     def queryGoodsRecord(self):
#         recordsList = []
#         for record in goodsRecords:
#             if self.userId == record["用户Id"]:
#                 recordsList.append(record)
#         if not recordsList:
#             return "当前用户没有购买记录！"
#         else:
#             return recordsList
#
#
# apple = Goods(1, "苹果", 30)
# pear = Goods(2, "梨子", 20)
# banana = Goods(3, "香蕉", 10)
# user1 = User(1, 100)
# user2 = User(2, 100)
# print(apple.amount)
# result = user1.deposit(100)
# print(result)
#
# goodslist1 = [apple, pear, banana, apple]
# goodslist11 = [banana]
# goodslist2 = [banana]
# result1 = user1.shopping(goodslist1)
# result11 = user1.shopping(goodslist11)
# result2 = user2.shopping(goodslist2)
# print(result1)
# print(result11)
# print(result2)
# print(goodsRecords)
# print(user1.queryGoodsRecord())
# print(user2.queryGoodsRecord())
# '''abcis bcd 哈哈哈  三引号更多用于方法的解释(多行解释)'''
#
# print(0b00001011)
# print(0b11)
# a=b=c=20
# b = 30
# print(a,id(a))
# print(b,id(b))
# print(c,id(c))
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst2 == lst1)
# print(lst2 is lst1)
# print(lst2 is not lst1)
# print(lst2 not lst1)
# score=80
# if 90<=score<=100:
#     print('A')
# if 90>score>=80:
#     print('B')
# a = 10
# b = 20
# print(f'{str(a)}大于等于{str(b)}' if a>=b else f'{str(a)}小于{str(b)}')
# if 2 > 1:
#     pass
# while True:
#     break
#     pass
# for _ in range(5):
#     print('abc')
# list2 = list(['hello','world',123])
# a = str('www')
# print(list2)
# print(a)
# list1 = [1,2,3,4,5,6,7]
# # print(list1[1:1])
# # list1[1:3] = []
# del list1[1:3]
# list1[2:5] = [30,40]
# print(list1)
# list1 = [1,2,4,5,1,3,8,1,6,55,0]
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)
# list1 = [1,2,4,5,1,3,8,1,6,55,0]
# newlist1 = sorted(list1)
# # print(list1)
# print(newlist1)
# desclist1 = sorted(list1,reverse = True)
# print(desclist1)
# list1 = [i*2 for i in range(1,10)]
# print(list1)
# list1 = list([1,2,3,4,5])
# print(list1)
# a = [1, 2, 3, 4, 5]
# a.append(123123)
# dict1 = {'1': "11",'list1': a[1:3], a: '键不可以为可变对象'}
# print(a)
# print(dict1)
# student = dict(name='jack', age=20)
# print(student)
# print(student['name'])
# print(student.get('name'))
# print(student.get('address','没有地址栏'))
# list1.clear()
# student.clear()
# print(student)
# student['address'] = '重庆'
# student['name'] = 'Tom'
# print(student)
# score = {'张三': 100, '李四': 98, '王五': 45}
# keys = score.keys()
# print(keys)
# print(type(keys))
# print(list(keys))
# values = score.values()
# print(values)
# print(type(values))
# print(list(values))
# items = score.items()
# print(items)
# print(list(items))
# for i in score.values():
#     print(i)
# for j in score:
#     print(j, score[j], score.get(j))
# keys = ['key1','key2','key3','key4','key5']
# values = ['value1','value2','value3']
# a = [1]
# b = [2]
# zip1 = zip(a,b)
# print(zip1)
# dict1 = {key:value for key,value in zip(keys,values)} #以短的那个为基数
# print(dict1)
#
# dict1 = {key:value for key,value in zip(range(5),range(10))} #以短的那个为基数
# print(dict1)
# tup = (1,2,3)
# print(tup,type(tup))
# tup2 = 1,2,3
# print(tup2,type(tup2))
# tup3 = tuple((1,2,3))
# print(tup3,type(tup3))
#
# list1 = [1,2,2,3,3,3,4,5]
# set1 = set(list1)
# print(set1,type(set1))
# set2 = {1,2,3,4,4,4} #集合会自动去重，集合无序，集合是没有value的字典
# print(set2,type(set2))
# set3 = set()
# print(type(set3))
# set4 = {1, 2, 3, 4}
# print(set4,type(set4))
# set1 = {1,2,3,4,5,66}
# set1.add(6)
# set1.update({7,8,9})
# set1.update((7,8,9))
# set1.update([7,8,9])
# set1.update()
# set1.remove(66)
# set1.discard(67)
# set1.pop() #集合无序，所以随机删除一个
# set1.clear()
# print(set1)
#
# set1 = {1,2,3,4,5,6}
# set2 = {1,2,3,4}
# set3 = {1,2,9}
# print(set2.issubset(set1))
# print(set3.issubset(set1))
# print(set1.issuperset(set2))
# print(set1.issuperset(set3))
# print(set2.isdisjoint(set3))
# set4 = {10,20,30,40}
# print(set2.isdisjoint(set4 ))
# set1 = {1,2,3,4}
# set2 = {2,3,4,5,6}
# print(set1.intersection(set2))
# print(set1 & set2)
# print(set1.union(set2))
# print(set1 | set2)
# print(set1.difference(set2))
# print(set1 - set2)
# print(set1.symmetric_difference(set2))
# list1 = [i for i in range(5)]
# print(list1)
# i = [1,2,3]
# j = [4,5,6]
# dict1 = {x:y for x,y in zip(i,j)}
# print(dict1)
# set1 = {i for i in range(5)}
# print(set1)
# a = '123'
# b = '456'
# c = a + b
# d = ''.join(['123','456'])
# e = 'abc'.join(['123','456'])
# print(c,d,e,id(c),id(d))
# s = 'hello,hello'
# print(s.index('lo'))
# print(s.rindex('lo'))
# print(s.find('lo'))
# print(s.rfind('lo'))
# print(s.find('k'))
# print(s.rfind('k'))
# s = 'hellO,pythoN'
# print(s.upper(),s.lower(),s.title(),s.swapcase(),s.capitalize())
# s = 'hello,python'
# print(s.center(20,'*'),s.center(20))
# print(s.ljust(20,'+'),s.ljust(20))
# print(s.rjust(20))
# print(s.zfill(20))
# s = 'hello world python'
# list1 = s.split()
# print(list1)
# s1 = 'hello|world|python'
# print(s1.split(sep='|'))
# print(s1.split(sep='|',maxsplit=1))
# print(s.rsplit())
# print(s.rsplit(sep=' ',maxsplit=1))
# s = 'hello,world'
# print(s.isidentifier(),'hello_123'.isidentifier())
# print('   \t\n\r'.isspace())
# print('zhangsanabc'.isalpha())
# print('123'.isdecimal())
# print('123四Ⅲ'.isnumeric())
# print('zhangsan123'.isalnum())
# s1 = 'hello,python,python,python'
# print(s1.replace('python','java',2))
#
# list1 = ['hello','python']
# tup1 = ('hello','java')
# print('|'.join(list1),' '.join(tup1))
# print('*'.join('java'))
#
# print('apple'>'app','apple'>'b')
# print(ord('a'),ord('b'))
# print(chr(97),chr(98))
# ==比较的是value值，is比较的是id内存地址
# name = 'zhangsan'
# age = 20
# print('我的名字是%s,今年%d岁'%(name,age))
# print('我的名字是{0},今年{1}岁,我真的叫{0}'.format(name,age))
# print(f'我的名字是{name},今年{age}岁')
# print('%10.2f'%3.1415)
# print('{1:10.3f}'.format(777,3.1415,888))
#
# GBK一个中文两个字节，UTF-8一个中文三个字节
# s = '天涯过此时'
# print(s.encode())
# print(s.encode(encoding='GBK'))
# print(s.encode(encoding='UTF-8'))
# #解码，byte表示一个二进制数据
# byte1 = s.encode()
# byte2 = s.encode(encoding='GBK')
# byte3 = s.encode(encoding='UTF-8')
# print(byte1.decode())
# print(byte2.decode(encoding='GBK'))
# print(byte3.decode(encoding='UTF-8'))
#
# def fun(a,*args):
#     print(args)
# fun()
# fun(1)
# fun(1,2,)
# fun(1,2,3)
# def fun1(**args):
#     print(args)
# fun1(a=1)
# fun1(a=1,b=2,c=3)
# def fun2(*args1,**args2):
#     print(args1,args2)
#     # pass
# fun2()
# fun2(1)
# fun2(a=1)
# fun2(1,a=1)
# fun2(1,2,3,a=4,b=5,c=6)
# list1 = [1,2,3]
# def fun(*args):
#     print(args)
# fun(*list1)
# def fun1(a,b,c):
#     print(a,b,c)
# fun1(*list1)
# dict1 = {'a':1,'b':2,'c':3}
# def fun1(a,b,c):
#     print(a,b,c)
# fun1(*dict1)
# fun1(**dict1)
# def fun2(**args):
#     print(args)
# fun2(**dict1)
# def fun3(a,b,c,d):
#     print(a,b,c,d)
# fun3(1,2,d=3,c=4)
# def fun4(a,b,*,c,d,**args):    #从星号后只能使用关键字参数
#     print(a,b,c,d)
#     print(a,b,c,d,args)
# fun4(1,2,d=4,c=3,e=5)
# def fun():
#     global age
#     age= 20
#     print(age)
# fun()
# print(age)
# def fun(n):
#     if n == 1:
#         return 1
#     else:
#         print(n)
#         return n*fun(n-1)
# print(fun(6))
#
# try:
#     a = int(input('请输入一个整数'))
#     b = int(input('请输入另一个整数'))
#     result = a/b
#     print(f'计算结果为：{result}')
# except ZeroDivisionError:
#     print('除数不能为零')
# except ValueError:
#     print('只能输入整数')
# finally:
#     print('再见')
# a = int(input('请输入一个整数'))
# b = int(input('请输入另一个整数'))
# result = a / b
# print(f'计算结果为：{result}')
# try:
#     a = int(input('请输入一个整数'))
#     b = int(input('请输入另一个整数'))
#     result = a/b
# except BaseException as cuo:
#     print('出错了', cuo)
# else: # 没出错才执行
#     print(result)
# import traceback #方便将异常输出到日志文件中
# try:
#     print('-------------------')
#     print(1/0)
# except:
#     traceback.print_exc()
# # print(1/0)
# print(12345,'abc')
# i = 1
# while i < 10:
#     print(i)
# class Student:
#     pass
#
# print(__name__== '__main__')
# import time
# time.sleep(1)
# print(__name__)
# def print_name(a):
#     b=a
#     print(__name__)
# print_name()
# print(id(print_name(1)))
# print(type(print_name(1)))
# print(print_name(1))
#
# class Student:
#     ABC = 'abc'
#     def __init__(self,name,age,adress):
#         self.name=name
#         self.age=age
#         self.adress = adress
#         # self.__adress=adress
#     def eat(self):
#         print(self.name+'在吃饭')
# #
# stu1 = Student('张三',20)
# stu2 = Student('张三',20)
# # print(id(stu1))
# # print(id(stu2))
# def show():
#     print('为实例对象单独创建方法')
# stu1.show = show
# stu1.show()
# stu1 = Student('张三',20,'重庆')
# print(dir(stu1))
# print(stu1.name)
# print(stu1._Student__adress)  #查看实例的私有 属性
#
# class school(Student):
#     def __init__(self,name,age,adress,time):
#         super().__init__(name,age,adress)
#         self.time = time
#     def info(self):
#         print(self.name,self.age,self.adress,self.time)
#     def eat(self):
#         super().eat()
#         print('吃香蕉')
#     def __str__(self):
#         print('重写父类方法')
#
# sch1 = school('张三',18,'重庆','12:00')
# sch1.eat()
# sch1.info()
# print(sch1.ABC)
# print(dir(sch1))
# sch1.__str__()
# 类的浅拷贝和深拷贝，深拷贝要重新创建新的子对象，浅拷贝只创建要拷贝的类
# import copy
# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# a1 = A()
# b1 = B()
# c1 = C(a1,b1)  # c1与a1,b1两个实例对象有关联
# c2 = copy.copy(c1)
# c3 = copy.deepcopy(c1)
# print(id(c1),id(c1.name),id(c1.age))
# print(id(c2),id(c2.name),id(c2.age))
# print(id(c3),id(c3.name),id(c3.age))
#
# class A:
#     @classmethod
#     def a(cls):
#         print(1)
#
#     @staticmethod
#     def b():
#         print(2)
#
#     def c(self):
#         print(3)
# A.a()
# A.b()
# print('------------')
# c1 = A()
# c1.a()
# c1.b()
# c1.c()
# print('------------')
# if __name__ == '__main__':
#     A.b()
# import math
# print(math.pow(2,3))
#
# print('这句话在其他模块中也会运行')
# def add(a, b):
#     return a+b
# if __name__ == '__main__':
#     print(add(10,20))      # 在其他模块中不会运行
#
# import os
# os.system('notepad.exe')
# os.system('calc.exe')
# os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
# print(os.getcwd())
# print(os.listdir('../lianxi01'))
# os.mkdir('newdir1')
# os.makedirs('A/B/C')
# os.rmdir('newdir1')
# os.removedirs('A/B/C')
# print(os.getcwd())
# os.chdir(r'D:\Program Files (x86)\PyCharm\lianxi\lianxi01\1')
# print(os.getcwd())
# os.chdir(r'D:\Program Files (x86)\PyCharm\lianxi\lianxi01')
# print(os.getcwd())
# import os.path
# print(os.path.abspath('1.txt'))
# 练习：获取一个目录下面的所有py文件
# import os
# path = os.getcwd()
# list1 = os.listdir(path)
# for filename in list1:
#     if filename.endswith('.py'):
#         print(filename)
# 遍历一个目录下的所有文件（包括子目录）
# import os
# path = os.getcwd()
# lst_files = os.walk(path)
# # print(lst_files)  # 通过walk方法得到的lst_files是一个迭代器对象，返回一个元祖
# for dirpath,dirname,filename in lst_files:
#
#     """ print(dirpath)
#     print(dirname)
#     print(filename)
#     print('-----------------------')"""
#     for dir in dirname:
#         print(os.path.join(dirpath,dir))
#     for file in filename:
#         print(os.path.join(dirpath,file))
#     print('************************')
#
# fp = open('2.txt','w')
# print('奋斗成就更好的你',file=fp)
# fp.close()
#
# with open('3.txt','w') as file:
#     file.write('奋斗成就更好的你')
#
# print('1234567890')
# print('\tabc1234567890')
# print('\ta\tbc\tfefh\tg')
#
# dict1 = {'a':'1','b':'2','c':'3','d':'4'}
# for key in dict1:
#     print(key,dict1[key])
# list1 = ['a','b','c','d']
# list2 = [1,2,3,4]
# for i,j in zip(list1,list2):
#     print(i,j)
# i = zip(list1,list2)
# print(list(i))
# print(list(zip(*i)))
# a,b = zip(*i)
# print(list(a),list(b))
#
# print('\033[0:35m可以答应出彩色的字\033[0:34m1234')
# print('abcdefg\033[m')
# print('1234567')
# print('\033[0:35m可以答应出彩色的字')
# print('\033[m必须取消颜色显示')
#
# num = 100
# print('%.2f'%num)
# print('{:.2f}'.format(num))
# bin1 = bin(num)
# print(bin1,type(bin1))
#
# print('整数2进制转换',bin(num))
# print('整数的6进制转换',oct(num))
# print('整数的16进制转换',hex(num))
#
# def fun():
#     num = int(input('请输入整数:'))
#     print('整数2进制转换',bin(num))
# if __name__ == '__main__':
#     while True:
#         try:
#             fun()
#             break
#         except:
#             print('请输入整数！')
#
# print(float(100),type(float(100)))
#
# 使用get()方法来获取字典，字典里没有这个键也不会报错。
# dict1 = {'a': 1,'b': 2}
# print(dict1['a'],dict1.get('a'),dict1.get('c'))
#
# import math
# for i in range(100,1000):
#     if math.pow(i%10,3)+math.pow(i//10%10,3)+math.pow(i//100,3) == i:
#         print(i)
#
# import random
# rand = random.randint(1,10)
# for i in range(1,11):
#     num = int(input('请输入一个1——10之间的随机数：'))
#     if num<rand:
#         print('min')
#     elif num>rand:
#         print('max')
#     else:
#         print('相等')
#         break
# print(f'您一共猜了{i}次')
#
# for i in range(5,-1,-1):
#     print(i)
#
# list1 = ['a','b','c']
# list2 = [1,2,3]
# zip1 = dict(zip(list1,list2))
# print(zip1)
# zip2 = zip(list1,list2)
# for i in zip2:
#     print(i)
#
# list1 = ['a','b','c','d','e']
# print(list(enumerate(list1)))
# for index,item in enumerate(list1):
#     print(index,item)
#
# try:
#     a = '1'
#     if 0 < a < 10:
#         print('正常操作')
#     else:
#         raise Exception('主动抛出异常')
# except Exception as e:
#     print(e)
#
# print('-'*30)
#
# # 模拟高铁售票系统
# import prettytable as pt
# # 显示座位
#
#
# def show_ticket(row_num):
#     tb = pt.PrettyTable()
#     tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
#     for i in range(row_num):
#         lst = [f'第{i+1}行', '有票', '有票', '有票', '有票', '有票']
#         tb.add_row(lst)
#     print(tb)
#
# # 订票
# def order_ticket(row_num,row,column):
#     tb = pt.PrettyTable()
#     tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
#     for i in range(row_num):
#         if int(row) == i+1:
#             lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
#             lst[int(column)] = '已售'
#             tb.add_row(lst)
#         else:
#             lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
#             tb.add_row(lst)
#     print(tb)
#
# if __name__ == '__main__':
#     row_num = 13
#     # show_ticket(row_num)
#     choose_num = input('请输入选择的座位，如13,5表示13排5号座位')
#     try:
#         row,column = choose_num.split(',')
#     except:
#         print('输入格式有误')
#     order_ticket(row_num,row,column)
#
# import time
# def show_info():
#     print('输入提示数字，执行相应操作：0.退出 1.查看登陆日志')
#
# # 追加日志
# def write_logininfo(username):
#     with open('log.txt','a') as file:
#         s = f'用户名：{username},登陆时间：{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))}'
#         file.write(s)
#         file.write('\n')
#
# # 读取日志
# def read_logininfo():
#     with open('log.txt','r') as file:
#        print(file.read())
#         # while True:
#         #     line = file.readline()
#         #     if line == '':
#         #         break
#         #     else:
#         #         print(line,end='')
#
# if __name__ == '__main__':
#     username = input('请输入用户名：')
#     pwd = input('请输入密码：')
#     if 'admin' == username and 'admin' == pwd:
#         print('登陆成功！')
#         write_logininfo(username)  #记录日志
#         show_info() #提示用户要执行什么操作
#         num = int(input('请输入操作数字：'))
#         while True:
#             if num == 0:
#                 print('退出成功')
#                 break
#             elif num == 1:
#                 print('查看登陆日志')
#                 read_logininfo() #读取日志
#                 num = int(input('请输入操作数字：'))
#             else:
#                 print('您输入的数字有误！')
#                 show_info()
#                 num = int(input('请输入操作数字：'))
#     else:
#         print('对不起，用户名或密码不正确！')
#
#     '''print(time.time())
#     print(time.localtime(time.time()))
#     print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))'''
#
# with open('reply.txt', 'a') as file:
#     file.write('订单|如果您有任何订单问题，可以登陆淘宝账号，点击“我的订单”，查看订单详情\n')
#     file.write('物流|如果您有任何物流问题，可以登陆淘宝账号，点击“我的订单”，查看物流详情\n')
#     file.write('账户|如果您有任何账户问题，可以联系淘宝客服，电话:XXXX-xxxx\n')
#     file.write('支付|如果您有任何支付问题，可以联系支付宝客服，QQ:xxxxxx\n')
#
# def find_answer(question):
#     with open('reply.txt','r',encoding='GBK') as file:
#         while True:
#             line = file.readline()
#             if not line: # if line == ''到文件末尾退出
#                 break
#             # 字符串的分割
#             keyword = line.split('|')[0]
#             reply = line.split('|')[1]
#             if keyword in question:
#                 return reply
#         return False
#
# if __name__ == '__main__':
#     question = input('Hi，您好，小蜜在这里等主人很久了，有什么烦恼快和小蜜说吧')
#     while True:
#         # 开始在文件中查找
#         if question == 'bye':
#             break
#         reply = find_answer(question)
#         if not reply:
#             question = input('小蜜不知道您在说什么，您可以问一些关于订单、物流、账户、支付等问题。（退出请输入bye）')
#         else:
#             print(reply)
#             question = input('小主，您还可以继续问一些关于订单、物流、账户、支付等问题。（退出请输入bye）')
#     print('小主再见')
#
# str1 = "{'a':1,'b':2,'c':3}"
# print(type(str1))
# dict1 = dict(eval(str1))
# print(type(dict1))
# print(dict1['a'])
#
# a = '[1, 2, 3, 4, 5, 6]'
# b = '(1, 2, 3, 4, 5, 6)'
# c = '{1, 2, 3, 4, 5, 6}'
# d = "{'a': 1, 'b': 2, 'c': 3}"
# e = '1, 2, 3, 4, 5, 6'
# print(type(a), type(b), type(c), type(d), type(e))
# aa = eval(a)
# bb = eval(b)
# cc = eval(c)
# dd = eval(d)
# ee = eval(e)
# print(ee, type(ee))
# abc = str(e)
# print(abc, type(abc))
# import time
# import os.path
# import time

# with open(r'../games/1.txt','r') as file:
#     print(file.readline())
# print(int(12.978))
# print(bool(0))
# print(10//9)

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# while True:
#     pass
#
# element = driver.find_element(By.ID, 'sb_form_q')
# element.send_keys('WebDriver')
# element.submit()
#
# # time.sleep(5)
# # driver.quit()

# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
#
# # 设置浏览器参数
# option = webdriver.EdgeOptions()
# option.add_experimental_option("detach", True)
#
# # 打开浏览器驱动
# s = Service(executable_path=r'D:\Python\Scripts\msedgedriver.exe')
# # 把浏览器参数传入到网页驱动
# web = webdriver.Edge(options=option, service=s)
# driver = webdriver.Edge()
# driver.get('https://bing.com')


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()
# driver.get('https://www.bilibili.com/')
# driver.find_element(By.CLASS_NAME,'nav-search-input').send_keys('软件测试老白')
# driver.find_element(By.CLASS_NAME,'nav-search-btn').click()
# time.sleep(3)
# driver.close()

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.baidu.com/')
# driver.find_element(By.ID, 'kw').send_keys('selenium')
# driver.find_element(By.ID, 'su').click()
# time.sleep(5)

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.bilibili.com/')
# driver.find_element(By.CLASS_NAME,'nav-search-input').send_keys('新年快乐')
# driver.find_element(By.CLASS_NAME,'channel-link').click()
# driver.find_elements(By.CLASS_NAME,'channel-link')[4].click()
# for ele in driver.find_elements(By.CLASS_NAME,'channel-link'):
#     print(ele.text)
# time.sleep(3)

# driver =webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.bilibili.com/')
# driver.find_element(By.TAG_NAME,'input').send_keys('学习selenium')
# time.sleep(3)

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.baidu.com/')
# # driver.find_element(By.NAME,'wd').send_keys('根据name属性定位')
# driver.find_elements(By.NAME,'wd')[0].send_keys('根据name属性定位')
# time.sleep(3)

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.baidu.com/')
# # driver.find_element(By.LINK_TEXT,'新闻').click()
# # driver.find_elements(By.LINK_TEXT,'新闻')[0].click()
# # driver.find_element(By.PARTIAL_LINK_TEXT,'新闻').click()
# driver.find_elements(By.PARTIAL_LINK_TEXT,'新闻')[0].click()
# time.sleep(3)

# 根据样式选择器定位
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.baidu.com/')
# driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('selenium')
# driver.find_element(By.CSS_SELECTOR, '#su').click()
# driver.find_element(By.CSS_SELECTOR, '.hot-refresh-text').click()
# driver.find_element(By.CSS_SELECTOR, '[name="wd"]').send_keys('selenium')
# driver.find_element(By.CSS_SELECTOR, '[autocomplete="off"]').send_keys('selenium')
# driver.find_element(By.CSS_SELECTOR, '[id="kw"]').send_keys('selenium')
# driver.find_element(By.CSS_SELECTOR, '[class="s_ipt"]').send_keys('selenium')
# driver.find_element(By.CSS_SELECTOR, 'a[href="http://news.baidu.com"]').click()
# driver.find_element(By.CSS_SELECTOR, 'input[class="s_ipt"]').send_keys('selenium')
# driver.find_element(By.CSS_SELECTOR, 'input[id="kw"]').send_keys('selenium')
# driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="off"]').send_keys('selenium')
# driver.find_element(By.CSS_SELECTOR, 'a[href*="news.baidu"]').click()
# driver.find_element(By.CSS_SELECTOR, 'a[href^="http://news"]').click()
# driver.find_element(By.CSS_SELECTOR, 'a[href$="news.baidu.com"]').click()
# driver.find_element(By.CSS_SELECTOR, 'input.s_ipt').send_keys('123456')
# 分级定位子元素（直接右键复制）
# driver.find_element(By.CSS_SELECTOR, '#s-top-left > a:nth-child(4)').click()
# time.sleep(3)

# 通过xpath定位
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.baidu.com/')
# driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/div[1]/a[1]').click()
# driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys('selenium')
# driver.find_element(By.XPATH,'//input[@class="s_ipt"]').send_keys('selenium')
# driver.find_element(By.XPATH,'//input[@name="wd"]').send_keys('selenium')
# driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('selenium')
# time.sleep(3)

# 多个属性组合定位
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.baidu.com/')
# driver.find_element(By.XPATH, '//input[@name="wd" and @class="s_ipt" and @autocomplete="off"]').send_keys('selenium')
# # driver.find_element(By.XPATH, '//div[@id="s-top-left"]/a[4]').click()
# # driver.find_element(By.XPATH, '//div[@id="s-top-left"]/../div[3]').click()
# time.sleep(3)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.iviewui.com/view-ui-plus/component/form/radio')
# driver.find_elements(By.XPATH, '//input[@class="ivu-radio-input" and @type="radio"]')[1].click()
# time.sleep(2)
# driver.find_elements(By.XPATH, '//input[@class="ivu-radio-input" and @type="radio"]')[2].click()
# time.sleep(2)
# driver.find_elements(By.XPATH, '//input[@class="ivu-radio-input" and @type="radio"]')[3].click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//span[text()="Android"]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//span[text()="Windows"]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//span[text()="Android"]/preceding-sibling::span/input').click()
# time.sleep(2)

# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://sahitest.com/demo/selectTest.htm')
# time.sleep(2)
# select = Select(driver.find_element(By.ID, 's1'))
# # select.select_by_index(1)
# # select.select_by_value('51')
# select.select_by_visible_text('Cell Phone')
# time.sleep(2)

# 级联选择
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://www.iviewui.com/view-ui-plus/component/form/cascader')
# time.sleep(1)
# driver.find_element(By.XPATH, '//input[@class="ivu-input ivu-input-default"]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//li[contains(text(),"北京")]').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '//li[contains(text(),"王府井")]').click()
# time.sleep(2)

# 时间日期选择 driver = webdriver.Chrome() driver.maximize_window() driver.get(
# 'https://www.iviewui.com/view-ui-plus/component/form/date-picker') driver.find_element(By.XPATH,
# '//input[@class="ivu-input ivu-input-default ivu-input-with-suffix"]').send_keys('2023-09-13') time.sleep(2)
# driver.find_elements(By.XPATH, '//input[@class="ivu-input ivu-input-default ivu-input-with-suffix"]')[1].send_keys(
# '2023-09-14 - 2023-10-31') time.sleep(2)

# 弹窗选择
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://sahitest.com/demo/promptTest.htm')
# time.sleep(1)
# driver.find_element(By.XPATH, '//input[@name="b1"]').click()
# time.sleep(1)
# driver.switch_to.alert.send_keys('测试alert')
# time.sleep(1)
# # driver.switch_to.alert.accept()
# # time.sleep(1)
# driver.switch_to.alert.dismiss()
# time.sleep(1)

# 文件上传
# from utils.get_filepath import get_reply_path
# path = get_reply_path()
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://sahitest.com/demo/php/fileUpload.htm')
# time.sleep(1)
# driver.find_element(By.ID, 'file').send_keys(r'{}'.format(path))
# time.sleep(1)
# driver.find_element(By.NAME, 'submit').click()
# time.sleep(3)

# 文件下载
# if os.path.exists(r'../file/chromedriver_win32.zip'):
#     os.remove(r'../file/chromedriver_win32.zip')
#     print('文件已删除')
# chromeOptions = webdriver.ChromeOptions()
# prefs = {"download.default_directory": r"D:\Program Files (x86)\PyCharm\lianxi\file"}
# chromeOptions.add_experimental_option('prefs', prefs)
# driver = webdriver.Chrome(chromeOptions)
# driver.maximize_window()
# driver.get('http://chromedriver.storage.googleapis.com/index.html')
# time.sleep(1)
# driver.find_element(By.XPATH, '/html/body/table/tbody/tr[152]/td[2]/a').click()
# time.sleep(1)
# driver.find_element(By.XPATH, '/html/body/table/tbody/tr[7]/td[2]/a').click()
# time.sleep(5)
# # driver.implicitly_wait(10)

# 切换窗口
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://sahitest.com/demo/iframesTest.htm')
# time.sleep(1)
# driver.find_element(By.ID, 'checkRecord').clear()
# time.sleep(1)
# driver.find_element(By.ID, 'checkRecord').send_keys('666')
# time.sleep(1)
# driver.switch_to.frame(1)
# driver.find_element(By.ID, "open-self").click()
# time.sleep(3)

# driver = webdriver.Chrome() driver.maximize_window() driver.get(r'file:C:\Users\24512\Documents\Untitled-1.html')
# time.sleep(1) driver.find_element(By.ID, 'checkRecord').clear() time.sleep(1) driver.find_element(By.ID,
# 'checkRecord').send_keys('666') time.sleep(1) # driver.switch_to.frame("iframe_id") driver.switch_to.frame(
# "iframe_name") driver.find_element(By.CSS_SELECTOR, '#i_cecream > div.bili-feed4 > div.bili-header.large-header >
# div.bili-header__channel > div.right-channel-container > div.channel-items__left > a:nth-child(1)').click()
# time.sleep(3)

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://sahitest.com/demo/iframesTest.htm')
# driver.find_element(By.ID, 'checkRecord').clear()
# time.sleep(1)
# driver.find_element(By.ID, 'checkRecord').send_keys('666')
# ele = driver.find_element(By.CSS_SELECTOR, 'body>iframe')
# driver.switch_to.frame(ele)
# time.sleep(1)
# # driver.switch_to.parent_frame()
# driver.switch_to.default_content()
# driver.find_element(By.ID, 'checkRecord').clear()
# time.sleep(1)
# driver.find_element(By.ID, 'checkRecord').send_keys('777')
# time.sleep(2)


# 商城后台管理系统实践
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://sellshop.5istudy.online/sell/user/logout')
# # 输入账号
# driver.find_element(By.ID, 'username').send_keys('123456')
# # 输入密码
# driver.find_element(By.ID, 'password').send_keys('123456')
# # 点击登录
# driver.find_element(By.CSS_SELECTOR, 'input[value="登录"]').click()
# time.sleep(1)
# # 新增商品
# driver.find_element(By.CSS_SELECTOR, '#sidebar-wrapper > ul > li:nth-child(3) > ul > li:nth-child(3) > a').click()
# # 商品名称
# driver.find_element(By.CSS_SELECTOR, '#page-content-wrapper > div > div > div > form > div:nth-child(1) > input').send_keys('壁纸')
# # 商品价格
# driver.find_element(By.CSS_SELECTOR, '#page-content-wrapper > div > div > div > form > div:nth-child(2) > input').send_keys('10')
# # 商品库存
# driver.find_element(By.CSS_SELECTOR, '#page-content-wrapper > div > div > div > form > div:nth-child(3) > input').send_keys('1')
# # 商品描述
# driver.find_element(By.CSS_SELECTOR, '#page-content-wrapper > div > div > div > form > div:nth-child(4) > input').send_keys('很好看')
# # 商品图片
# (driver.find_element(By.CSS_SELECTOR, '#page-content-wrapper > div > div > div > form > div:nth-child(5) > input').
#  send_keys('https://tse3-mm.cn.bing.net/th/id/OIP-C.aKP-w7X4jOh7yjOkpzkgXQHaEK?w=317&h=180&c=7&r=0&o=5&dpr=1.4&pid=1.7'))
# # 商品类目
# select = Select(driver.find_element(By.CSS_SELECTOR, '#page-content-wrapper > div > div > div > form > div:nth-child(6) > select'))
# select.select_by_value('74')
# time.sleep(3)
# # 点击提交
# driver.find_element(By.CSS_SELECTOR, '#page-content-wrapper > div > div > div > form > button').click()
# time.sleep(2)

# import pytest
# pytest.main()
# pytest.main(['test_pytest.py', '-v'])


# 用python进行接口测试
# import requests
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')  # 解决请求返回response编码错误问题
# r = requests.get('http://api.github.com/events')
# print(r.status_code)
# print(r.json())
# print(r.text)
# params = {"shouji": '13456755448', 'appkey': '0c818521d38759e1'}
# r = requests.get(url='http://sellshop.5istudy.online/sell/shouji/query', params=params)
# print(r.status_code)
# print(r.json())
# params = {"shouji": '13456755448', 'appkey': '0c818521d38759e1'}
# r = requests.post(url='http://sellshop.5istudy.online/sell/shouji/query', params=params)
# print(r.status_code)
# print(r.json())
# json_data = {'title': 'foo', 'body': 'bar', 'userId': '1'}
# r = requests.post(url='http://jsonplaceholder.typicode.com/posts', json=json_data)
# print(r.status_code)
# print(r.json())
# config_data = {'text': 'hello'}
# r = requests.post(url='https://dict.youdao.com/keyword/key', config_data=config_data)
# print(r.status_code)
# print(r.json())
# url = 'https://movie.douban.com/j/search_subjects'
# params = {
#     'type': 'movie',
#     'tag': '热门',
#     'page_limit': '50',
#     'page_start': '0'
# }
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69"}
# r = requests.get(url=url, params=params, headers=headers)
# print(r.status_code)
# print(r.json())


# pytest参数化parametrize
# import pytest


# 单参数，单次循环
# @pytest.mark.parametrize('key', ['value'])
# def test_parametrize1(key):
#     print('我是' + key)
#
#
# @pytest.mark.parametrize('name', ['老白'])
# def test_parametrize2(name):
#     print('我是' + name)

# 单参数，多次循环
# 运行时将数组里的值分别赋值给变量，每赋值一次，运行一次
# @pytest.mark.parametrize('name', ['安琪拉', '黄忠', '大乔'])
# def test_parametrize2(name):
#     print('我是' + name)
#
# 多个参数多个循环，value值列表里面必须再嵌套 列表\元组
# @pytest.mark.parametrize('name,word', [['安琪拉', '火烧屁屁咯'], ['黄忠', '周日被我射熄火了'], ['小乔', '我不是大乔']])
# def test_parametrize(name, word):
#     print(f'{name}的台词是{word}')
#
#
# @pytest.mark.parametrize('name,word', [('安琪拉', '火烧屁屁咯'), ('黄忠', '周日被我射熄火了'), ('小乔', '我不是大乔')])
# def test_parametrize(name, word):
#     print(f'{name}的台词是{word}')
#
#
# # 如果有多个参数的情况如果值只写['安琪拉', '火烧屁屁咯']会报错，必须要嵌套列表或元组
# @pytest.mark.parametrize('name,word', [('安琪拉', '火烧屁屁咯')])
# def test_parametrize(name, word):
#     print(f'{name}的台词是{word}')
