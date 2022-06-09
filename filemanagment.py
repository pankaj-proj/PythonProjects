import logging
import sys

from decorator import logfunctionexecution

class filemanagment:
    @logfunctionexecution
    def replace_text(self,inputfile, fromstring, tostring):

        logging.info('start replace_text method from string' + fromstring + ' to string ' + tostring)
        try:
            with open(inputfile) as r:
                text = r.read().replace(fromstring, tostring)  # open file and replace value
            with open(inputfile, "w") as w:
                w.write(text)
        except Exception as e:
            logging.error('Exception while updating file content ' + e)