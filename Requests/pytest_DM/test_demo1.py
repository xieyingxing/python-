class TestDome:

    def setup_class(self):  #类级别的setup；不加class则有几个函数就执行几遍
        print('setup')

    def teardown_class(self):  #；类级别的teardown
        print('teardown')

    def test_a(self):
        print('a')
        # assert 1  #断言为真

    def test_b(self):
        print('b')
        # assert 0  #断言为假

    def test_c(self):
        a = 1
        b = 2
        print(a + b)


