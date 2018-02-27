# encoding=UTF-8
# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
'''P116 异常处理 Exception

    程序出现例外情况，就会发生异常，要通过使用异常来处理；
    如文件不存在、无效语句、错误拼写，
    python会抛出Raise错误Error或语法错误
    python会反革命出检测到错误发生的位置，就是错误处理器Error Handler
    通过try..except来处理异常情况，通常把语句放在try代码块中
'''
try:
    text=input("Enter something -->")
except EOFError:    #捕获输入时按了Ctrl+D加了文件结尾符号End of File
    print("Why did you do an EOF on me ?")
except KeyboardInterrupt:   #捕获Ctrl+C
    print("You cancalled the operation.")
else:
    print("You entered {}.".format(text))

# P118 抛出异常
"""可以通过Raise语句来引发一次异常，具体方法是提供错误名
或异常名以及要抛出Thrown异常的对象
可以引发的错误或异常必须是直接或间接从属于Exception异常类的派生类
"""
class ShortInputException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atlease=atleast
        # 自定义异常类型，判断输入文本长度及期望最小长度
try:
    text=input("Enter something --> ")
    if len(text) < 3:
        raise ShortInputException(len(text),3)
except EOFError:
    print("why did you do an EOF on me?")
except ShortInputException as ex:
    print(('ShorInputExcetion: The input was' +
          '{0} long,expected at least {1}').format(
              ex.length,ex.atleast))
else:
    print('No exceptioin was raised.')