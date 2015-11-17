#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
def printme(str):
    print str;
    return;


# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");
printme("");
pass


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print "函数内取值: ", mylist
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print "函数外取值: ", mylist
