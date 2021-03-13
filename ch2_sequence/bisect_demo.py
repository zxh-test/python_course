# -*- coding:utf-8 -*-
import bisect
import sys

# todo random.seed
# todo random.randrange(num*2)

"""
bisect 是基于二分查找法实现的模块 ，
作用： 在一个有序列表中插入元素并保持列表为有序状态、或返回插入位置但并不进行实际的插入。
包含了6个函数： ['bisect', 'bisect_left', 'bisect_right', 'insort', 'insort_left', 'insort_right']

"""

data = [9, 7, 10, 2, 88]
data.sort()
bisect.insort(data, 1)  # insort 按顺序插入元素，不会改变原有排序
data  # [1, 2, 7, 9, 10, 88],  就地排序 插入，不创建新对象

bisect.bisect(data, 0)  # 0:  返回数字0 要插入的位置， 但不会真的插入

bisect.bisect_left(data, 7)  # : 2, 插入重复的情况， 插入x左侧的位置
bisect.bisect_right(data, 7)

bisect.insort_left(data, 7)  # 会进行实际插入


# 实际应用 把分数和成绩等级对用起来

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


result = [grade(score) for score in [33, 44, 55, 66, 60, 77, 88, 99]]

tuple_data = (1, 2, 3, 4)
print(bisect.insort(tuple_data, 2))
print(tuple_data)



