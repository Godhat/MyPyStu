# encoding=UTF-8
# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
'''P122 标准库 Python Standrad Library
    
    1、标准库是Python安装包的一部分；
    2、通过安装包文件的库概览Library Reference可查找所有模块全部细节
'''
# sys 模块 （包括一些针对特定系统的功能），如前期的sys.argv
import sys
print(sys.version_info)
print("IS python version 3 : ",sys.version_info.major==3)

# logging 模块
import os
import platform
import logging
if platform.platform().startswith('Windows'):
    logging_file=os.path.join(os.getenv('HOMEDRIVER'),
                              os.getenv('HOMEPATH'),
                              'test.log')
else:
    logging_file=os.path.join(os.getenv('HOME'),
                              'test.log')
    #os.path.join()函数将位置信息聚合一起，会确保完整路径符合当前OS的预期格式
print("Logging to ",logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w')

logging.debug("Start of program ")
logging.info("Doing something ")
logging.warning("Dying now")

'''
➜  ~ pwd
/Users/DavidTai
➜  ~ cat test.log
2018-02-27 17:46:55,870 : DEBUG : Start of program 
2018-02-27 17:46:55,871 : INFO : Doing something 
2018-02-27 17:46:55,871 : WARNING : Dying now
➜  ~ 
'''