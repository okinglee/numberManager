__author__ = 'YanqingLee'
import leancloud
engine = leancloud.Engine(getCurrentNumber)

@engine.define
def getCurrentNumber(userName):
    return 12345678