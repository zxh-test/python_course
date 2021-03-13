import pytest
"""
SETUP    S session_scope
    SETUP    M module_scope
        SETUP    F func_scope
        test_scope.py::test_1 (fixtures used: func_scope, module_scope, session_scope).
        TEARDOWN F func_scope
        SETUP    F func_scope
        test_scope.py::test_2 (fixtures used: func_scope, module_scope, session_scope).
        TEARDOWN F func_scope
      SETUP    C class_scope
        test_scope.py::TestSometing::test_3 (fixtures used: class_scope).
        test_scope.py::TestSometing::test_4 (fixtures used: class_scope).
      TEARDOWN C class_scope
    TEARDOWN M module_scope
TEARDOWN S session_scope
"""

@pytest.fixture(scope='function')
def func_scope():
    """作用于函数范围的装饰器"""


@pytest.fixture(scope='class')
def class_scope():
    """作用于类范围的装饰器"""


@pytest.fixture(scope='module')
def module_scope():
    """作用于模块范围内的装饰器"""


@pytest.fixture(scope='session')
def session_scope():
    """作用于会话范围内的装饰器"""


def test_1(func_scope, module_scope, session_scope):
    pass


def test_2(func_scope, module_scope, session_scope):
    pass


@pytest.mark.usefixtures('class_scope')
class TestSometing():
    def test_3(self):
        pass

    def test_4(self):
        pass


if __name__ == '__main__':
    pytest.main(['--setup-show'])
