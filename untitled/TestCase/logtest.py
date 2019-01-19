import  logging,os
import logging.config
from  TestCase.logtest1 import test
#print(os.path.abspath(os.path.dirname(os.getcwd())))
config=os.path.join(os.path.dirname(os.path.abspath('.')),'common\\config.ini')
logging.config.fileConfig(config)
log1=logging.getLogger()
log2=logging.getLogger('wyq')
log1.error('123')
log2.debug('456')

print (os.path.abspath(os.path.join(os.getcwd(), "../..")))
print(os.path.dirname(__file__))