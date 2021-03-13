# 第一章pytest入门
## 常用命令：
        1. 帮助文档： pytest --help
        2. 查看哪些测试用例会被执行： pytest --collect-only
        3. 执行指定用例： pytest -k， 也可以使用表达式
        4. 测试用例分组：@pytest.mark.xxx, pytest -m xxx
           支持使用and, or, and not
        5. 遇到失败停止 pytest -x

## 参数化与数据驱动
# 第三章 pytest fixture
## fixture 常用用法
#### 回溯fixture执行过程：
        --setup-show
#### 使用fixture传递测试数据
        fixture可以return 任何类型的测试数据供 其他fixture或测试函数使用
        如：可以构造测试前的初始数据
#### 使用多个fixture
        pass
#### 指定fixture作用范围
        使用scope指定fixture作用范围
#### 使用usefixtures指定fixture
        与在测试方法中添加fixture参数相比，区别在于后者才可以使用fixture的返回值
        @pytest.mark.usefixtures() 常用于类上
#### fixture的autouse参数
        使用autouse=True，可以使作用域内的参数函数都运行该fixture
        不必再测试方法中再次添加 fixture参数， 但这种方式不常用
#### fixture重命名
        @pytest.fixture(name='new_name')
#### fixture的参数化
        fixture的params指定参数列表
        request也是fixture的内置fixture，他的param字段会被param参数列表的一个元素填充
        也可以指定ids,生成测试函数的标识
# 第四章内置fixture
#### 使用tmpdir与tmpdir_factory
        1. 这两个fixture负责在测试开始前创建临时文件目录，并在测试结束删除
        2. tmpdir是函数级， tmpdir_factory是会话级
        3. 单个测试使用tmpdir, 多个使用tmpdir_factory
#### tmpdir
        pass
#### tmpdir_factory
        pass
#### 使用pytestconfig
        pass
#### 使用cashe
        pass



