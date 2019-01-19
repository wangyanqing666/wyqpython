import  logging,os
import logging.config
config=os.path.join(os.path.dirname(os.path.abspath('.')),'common\\config.ini')
logging.config.fileConfig(config)
log1=logging.getLogger()
def test():
    log1.debug('111111111111')