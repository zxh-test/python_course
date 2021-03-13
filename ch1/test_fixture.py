# -*- coding: utf-8 -*-
import pytest

# ----------------------fixture简单使用------------------------------------
"""
1. 函数名字被当做参数传入时， 函数名字是一个变量。指向了存储函数的地址
2. 如果测试函数的参数列表中包含了fixture名字，那么pytest会检测到，并在测试函数之前执行
3. 将fixture执行结果 返回给fixture 名字
"""


@pytest.fixture()
def some_data():
    return 42


def test_some_data(some_data):
    print("some_data = ", some_data)  # some_data = 42
    assert some_data == 42


# -----------------------内置fixture----------------------------------
"""
1. tmpdir 内置装饰器 用来生成临时文件，最多生成3个，3个后前面的会被删除
"""


def test_tmpdir(tmpdir):
    print(tmpdir)  # tmpdir生成目录的路径


# ------------------------fixture传递测试数据-----------------------------

@pytest.fixture()
def a_tuple():
    return (1, 'a', None, {'bar': 23})


def test_a_tuple(a_tuple):
    assert a_tuple[3]['bar'] == 23


# -----------------------fixture 参数化-------------------------------

some_datas = ([1, 2, 3], [1, 1, 2], [2, 2, 4])


def id_func(fixture_value):  # ---------ids参数使用--------------------
    """id_func()调用单个some_datas对象"""
    print(fixture_value)
    return "{}".format(fixture_value)


@pytest.fixture(params=some_datas, ids=id_func)
def add_data(request):
    return request.param


def test_add_data(add_data):
    assert add_data[2] == add_data[0] + add_data[1]
