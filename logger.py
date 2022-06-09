import logging
import sys

def configurelogger():
    # Create and configure logger
    logging.basicConfig(filename="applog.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
    # Creating an object
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.StreamHandler(sys.stdout)


