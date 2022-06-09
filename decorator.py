import logging as log
from datetime import datetime

def logfunctionexecution(func):
    def wrapper(*args,**kwargs):
        log.info("function " +func.__name__ +" call started " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        func(*args)
        log.info("function " + func.__name__ + " call ended " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    return wrapper

