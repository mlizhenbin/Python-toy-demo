#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

print "dict['Name']: ", dict['Name'];
print "dict['Age']: ", dict['Age'];

# modify
dict['Age'] = 8;  # update existing entry
dict['School'] = "DPS School";  # Add new entry

print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];

# delete
del dict['Name'];  # 删除键是'Name'的条目
dict.clear();  # 清空词典所有条目
del dict;  # 删除词典

print "dict['Age']: ", dict['Age'];
print "dict['School']: ", dict['School'];
