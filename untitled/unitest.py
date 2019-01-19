#encoding=utf-8
import unittest
from xml.etree.cElementTree import ElementTree as ET
suite=unittest.TestSuite()
doc=ET().parse(source='./data/config.xml')
li =doc.findall('./case/*')
for i in li :
    classname=i.tag.split('-')[0]
    methodname=i.tag.split('-')[1]
    print(classname)
    suite.addTest(classname(methodname))
    print(i.tag)
#print(doc.findall('./case/*'))
