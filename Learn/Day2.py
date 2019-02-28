#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 列表 list 有序可重复集合
fruit = ['apple', 'banana', 'pear', 'orange', 'apple']
print(f"origin : {fruit}")
print(fruit[1:3])
# 在末尾添加元素, 可以添加空类型
fruit.append('banana')
fruit.append(None)
print(f"append : {fruit}")
# 删除第一个匹配的元素, 若删除不存在的则会报错
fruit.remove('pear')
# fruit.remove('bear')
print(f"remove : {fruit}")
# 复制一个出来, 和原来的互不影响
fruit_copy = fruit.copy()
fruit.remove('banana')
print(f"copy-origin : {fruit}")
print(f"copy-new : {fruit_copy}")
# 统计某个元素的个数
count_element = 'apple'
count = fruit.count(count_element)
print(f"count.{count_element} : {count}")
# 获取集合长度
size = fruit.__len__()
print(f"size : {size}")
# 清空元素
fruit.clear()
print(f"clear : {fruit}")
