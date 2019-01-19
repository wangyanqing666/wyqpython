# coding=utf-8
import unittest
class unitest(unittest.TestCase):
    c=4
    def setUp(self):
        pass
   # @unittest.skipIf(c==5,"c=5时跳过该测试")
    def test_01(self):
        a=1
        b=2
        d=a+b
        print("test_01")
        self.assertEqual(d, '4', '用例失败')

   # @unittest.skipIf(False, 'reason')
    def test_02(self):
        self.assertEqual('1', '1')
        print("test_02")

   # @unittest.skip( '无条件')
    def test_03(self):
        self.assertEqual('1', '1')
        print("test_03")
    def test_04(self):
        self.assertEqual('1','1')
        print("test_04")
    def tearDown(self):
        pass

# if __name__ == '__main__':
#     #unittest.main()
#     suit=unittest.TestSuite()
#     suit.addTest(unitest('test_01'))
#     unittest.TextTestRunner().run(suit)
#
