# -*- coding:utf-8 -*-
"""元组拆包"""
import os

# _占位符 舍弃了路径值
_, filename = os.path.split('home/desktop/demo.json')

# 用 * 处理剩下来的元素， 在Python中 函数用*args 来获取不确定数量的参数

a, b, *c = range(5)
print(a, b, c)  # 0 1 [2, 3, 4]

# 可以出现在表达式的任意位置

*c, a, b = range(5)
print(a, b, c)  # 3 4 [0, 1, 2]

# 嵌套元组拆包
metro_ares = [
    ('z', 'jp', (21, 22)),
    ('x', 'us', (23, 24)),
    ('h', 'es', (25, 26))
]

for name, country, (num1, num2) in metro_ares:
    print(num2)

# 具名元组
from collections import namedtuple

City = namedtuple('City', 'city_name city_code city_area')
print(City._fields)
city_data = ('beijing', '123', 23333.777)
data1 = City._make(city_data)
data2 = City(*city_data)
assert data1 == data2

# 对序列使用 + *
board = [[1, 2, 3]] * 3
board[1][2] = 'x'
print(board) # [[1, 2, 'x'], [1, 2, 'x'], [1, 2, 'x']] 全部都变成了x, 因为列表内的三个引用指向了同一个对象
