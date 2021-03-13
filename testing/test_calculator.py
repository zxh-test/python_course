import pytest
import yaml

from pythoncode.Calculator import Calculator


# 参数化与数据驱动的区别？
# yaml保存测试数据的使用

def get_datas(path="./data/calc.yaml"):
    with open(path) as f:
        datas = yaml.safe_load(f)
    return datas


class TestCalc:
    dates: list = get_datas()

    def setup_class(self):
        self.calc = Calculator()
        print("用例执行")

    @pytest.mark.parametrize("a, b, result", dates["add"]["datas"],ids=[1, 2, 3])
    def test_add(self, a, b, result):
        """这个测试用例使用了参数化的方式"""
        assert result == self.calc.add(a, b)

    @pytest.mark.parametrize("a, b, result", [[8, 4, 2], [3, 1, 3]])
    def test_div(self, a, b, result):
        assert result == self.calc.div(a, b)

    @pytest.mark.parametrize("a, b", [[2, 0], [3, 0]])
    def test_raises_div(self, a, b):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)

    # todo: 相乘功能
    def test_multiplication(self, test_data):
        assert 2 == self.calc.multiplication(test_data[0], test_data[1])

    def test_subtraction(self):
        assert 6 == self.calc.subtraction(7, 1)

    def teardown_class(self):
        print("执行结束")


