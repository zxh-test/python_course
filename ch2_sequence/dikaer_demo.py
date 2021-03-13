# -*- coding:utf-8 -*-

"""列表推导式计算笛卡尔积"""

colors = ['red', 'yellow', 'black']
sizes = ['S', 'M', 'L']
# 列表里的元素是输入的可迭代类型的元素构成的元组
tshirts = [(color, size) for color in colors for size in sizes]

"""使用生成器表达式计算笛卡尔积"""

for tshirt in ('%s, %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)