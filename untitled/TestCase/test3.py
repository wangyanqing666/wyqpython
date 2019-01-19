# coding=utf-8
import unittest
import time
from  TestCase.unitest import unitest
import HTMLTestReportCN
filename = "./wyq.txt"
suit=unittest.TestSuite()
suit.addTest(unitest('test_01'))
suit.addTest(unitest('test_02'))
suit.addTest(unitest('test_03'))
suit.addTest(unitest('test_04'))
with open(filename,'w') as f:
    unittest.TextTestRunner(stream=f, descriptions='Report_description',verbosity=2).run(suit)


'''
# suit=unittest.TestSuite()
# suite1 = unittest.TestLoader().loadTestsFromTestCase(unitest)
# suit.addTest(suite1)
# unittest.TextTestRunner().run(suit)
'''
'''
suite1 = unittest.makeSuite(unitest)
unittest.TextTestRunner().run(suite1)
'''

'''
HTMLTestReportCN包使用
now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename = '../report/' + now + '_result.html'
Report_description='环境：{name}----地址{dizhi}'.format(name='测试环境',dizhi='192.168.0.1')
with open(filename,'wb') as f:
    runner = HTMLTestReportCN.HTMLTestRunner(stream=f, title='王燕青接口自动化测试报告', description='Report_description',verbosity=2,tester='王燕青')
    result=runner.run(suit)
    a=result.success_count  # 运行成功的数目
    b=result.testsRun  # 运行测试用例的总数
    c=result.failure_count  # 运行失败的数目
    print(a,b,c)

'''

'''
TextTestRunner引用使用
result = unittest.TextTestRunner(verbosity=2).run(suit)
print(result.testsRun)  #运行测试用例的总数
print(len(result.failures))  #运行失败的数目
print(len(result.unexpectedSuccesses))
#print(len(result.errors))
'''

