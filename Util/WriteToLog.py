import os
import sys
sys.path.insert(0, r'C:\Users\Hana Danis\Downloads\Bootcamp-automation\python\HtmlPro')
from Testes.test_home import *
class Log:  
    def write(self, mes):
        """ Hana, 2.1.23
        open file, write log"""
        os.chdir(r'C:\Users\Hana Danis\Downloads\Bootcamp-automation\python\HtmlPro\Logs')
        self.file = open('Log.txt', 'a')
        self.file.write(mes)
        self.file.flush()
        self.file.close()




