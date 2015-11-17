#!/usr/bin/python
# -*- coding: UTF-8 -*-

list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john', '测试']

print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个的元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表

index = 1
for l in list:
    index = index + 1
    if index == 3:
        del l
    else:
        print l

for l in tinylist:
    print l

for i in range(len(tinylist)):
    print tinylist[i]
