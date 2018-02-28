# encoding=UTF-8
# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
'''P120 with语句

    除了finally块释放资源,还可以with语句
'''
with open("poem.txt") as f:
    for line in f:
        print(line,end='')

"""
open函数与with语句，关闭文件的操作交由with open来自动完成。
原理是：with语句所使用的协议Protocol，会获取由open语句返回的对象，本例是thefile
它总会在代码块开始之前调用 thefile.__enter__函数，并总会在代码块执行完后调用thefile.__exit))
参考PEP 343可了解更加全面解释
"""