#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Python 的几大数据类型:
# 整型(255) 浮点型(10.24) 字符串(hi) 布尔(True|False) 空类型(None)

#  输出多行文本
print(r'''hello
a
b
world''')
# and or not 用法
print(True and False)
print(True or False)
print(not True)
x = None
print(x)
# 将 字符 转换为 Unicode 码
print(ord('a'))
# 将 Unicode 码转换为 字符
print(chr(91))
# Python 中几种特殊的表示:
# b'xxx': xxx 表示 二进制
# f'xxx' 或 F'xxx': xxx 表示 运行时运算求值的表达式 (f-string)
# r'xxx': xxx 表示 纯的字符串
# u'xxx': xxx 表示 Unicode 编码
# 将 字符 转换为 二进制
print('我'.encode('UTF-8'))
# 将 二进制 转换为 字符
print(b'\xe6\x88\xaa'.decode('UTF-8'))
print(b'\x64'.decode('UTF-8'))
print(u'\x64')
# 格式化占位符    替换内容
# %d        整数
# %'2'd     '2' 指的是在输出内容中, 格式化后的数据(至少)占的位数，多余的位数补'空格'
# %'03'd    '3' 指的是在输出内容中, 格式化后的数据(至少)占的位数，多余的位数补'0'
# %f        浮点数
# %'.2'f    '.2' 指的是格式化后的数据保留小数点后 '2', 位数不够的补'0'
# %s    字符串
# %x    十六进制整数
# %%    输出百分号
print(f'%2d-%03d' % (3, 1))
print('%.2f' % 3.1415926)
print('Hello, {0}, 成绩提升了 {1:.2f}%'.format('小明', 17.125))
print('growth rate: %d %%' % 7)
