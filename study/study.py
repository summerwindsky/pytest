#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py


strset = ["1", "2"]


def format():
    if True:
        print "Answer"
        print "True"
    else:
        print "Answer"
        # 没有严格缩进，在执行时会报错
        print "False"

        '''
        '''


def func():
    raw_input("按下 enter 键退出，其他任意键显示...\n")
    print "test!!"


def datatype():
    counter = 100  # 赋值整型变量
    miles = 1000.0  # 浮点型
    name = "John"  # 字符串

    print counter
    print miles
    print name

    a = b = c = 1
    a, b, c = 1, 2, "john"

    # 数据类型转换
    print int(1.0)
    print hex(23)
    print dict({1: 2, 3: 4})
    print set([1, 2, "dfd"])


def operator():
    a = 10
    b = 20
    # 逻辑运算   and or not
    if a and b:
        print "1 - 变量 a 和 b 都为 true"
    else:
        print "1 - 变量 a 和 b 有一个不为 true"


# 成员变量   in  not in

# 身份运算符  is  is not

def ricu():
    while 1:
        print "true"

    # while … else 在循环条件为 false 时执行 else 语句块：
    count = 0
    while count < 5:
        print count, " is  less than 5"
        count = count + 1
    else:
        print count, " is not less than 5"


def test():
    # 格式化
    print "My name is %s and weight is %d kg!" % ('Zara', 21)

    # string 内建函数
    "test".capitalize()

    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [1, 2, 3, 4, 5, 6, 7]
    print "list1[0]: ", list1[0]
    print "list2[1:5]: ", list2[1:5]
    list1.insert(1,3)
    print list1

#字典
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    del dict['Name']  # 删除键是'Name'的条目
    dict.clear()  # 清空词典所有条目
    del dict  # 删除词典
    # print "dict['Age']: ", dict['Age']
    # print "dict['School']: ", dict['School']

    import time;  # 引入time模块
    ticks = time.time()
    print "当前时间戳为:", ticks

    localtime = time.asctime(time.localtime(time.time()))
    print "本地时间为 :", localtime
    # 最后用time.strftime()方法，把刚才的一大串信息格式化成我们想要的东西
    print(time.strftime('%Y-%m-%d', time.localtime(time.time())))


def funcTest():
    # 可写函数说明
    def printinfo(arg1, *vartuple):
        "打印任何传入的参数"
        print "输出: "
        print arg1
        for var in vartuple:
            print var
        return;

    # 调用printinfo 函数
    printinfo(10);
    printinfo(70, 60, 50);

def lambdaTest():
    # 可写函数说明
    sum = lambda arg1, arg2: arg1 + arg2;

    # 调用sum函数
    print "相加后的值为 : ", sum(10, 20)
    print "相加后的值为 : ", sum(20, 20)

def modul():
    reload(locals())

def fileTest():
    file = open("d:/ahs.txt")
    print file.read()
    file.readlines()
    file1 = open("d:/test.txt", "wb")
    file1.writelines(strset)
    file1 = open("d:/test.txt", "r")
    print file1.read()

if __name__ == '__main__':
    # func()
    # datatype()
    # ricu()
    # test()
    # funcTest()
    # lambdaTest()
    # modul()
    fileTest()