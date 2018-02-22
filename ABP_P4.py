# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
# P68 模块 Modules
import ABP_P4_Module    #原书为module_using_sys.py
import os
import sys
print(os.getcwd())
ABP_P4_Module     #原书为在命令行$python module_using_sys.py we are arguments  

print()
# P70 按字节码编译的.pyc文件
"""更快完成导入，.pyc文件是独立于运行平台的
"""
# from..import语句
"""from sys import argv
直接将argv变量导入到程序，以避免每次都输入sys.argv
警告：尽量避免使用from...import，而应使用import语句，
以避免在程序中出现名称冲突，以便于代码可读性
"""
from math import sqrt
print('Square root of 16 is : ',sqrt(16))

# 模块的 __name__
"""每个模块都有一个名称，模块语句可以找到它所处模块的名称
模块是独立运行还是被导入进来运行，可通过模块的__name__属性来实现
"""
import ABP_P4_Module2
ABP_P4_Module2
# 直接在命令行执行$python ABP_P4_Module2.py则显示为...run by itself

# P71 编写自己的模块
import ABP_P4_mymodule
ABP_P4_mymodule.say_hi()
print('Version',ABP_P4_mymodule.__Verion__)

# P72 dir() 内置的dir函数返回由对象所定义的名称列表
"""
1、如果对象是一个模块，则列表包括函数内所定义的函数、类和变量
2、dir()接受参数，如果参数是模块名称，将返回指定模块的名称列表
3、如果没有参数，将返回当前模块的名称列表
"""

print(dir(sys))
print(dir())

# P74 包Packages
"""遵守程序的层次结构
1、变量位于函数内部
2、函数与全局变量位于模块内部
包是指一个包含模块与一个特殊__init__.py文件的文件夹，表明特别的文件夹及包含了python模块
"""

"""总结：
1、模块和函数都是可重用的程序
2、包是组织模块的另一种层次结构
3、python标准库就是一组有关包与模块的例子
"""
