# encoding=UTF-8
# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
'''P119 Try ... Finally
    
    无论是否会发生异常，都可通过finally块来完成
'''
import sys
import time

f=None
try:
    f=open("poem.txt")
    while True:
        line=f.readline()
        if len(line)==0:
            break
        print(line,end='')
        sys.stdout.flush()
        print("Press ctrl+c now")
        time.sleep(2)
except IOError:
    print("Could not find file peom.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up : Closed the file)")

"""
此程序这样工作的：
按通常文件读取进行操作，使用time.sleep函数任意在每打印一行休2秒，
使用得程序运行非常缓慢，当程序正在运行时，按Ctrl+C中断或取消程序
KeyboardInterrupt异常被抛出，尔后程序退出。
退出程序前，finally子句会执行，文件对象总是被关闭。
print 之后使用sys.stout.flush()，以便立即打印到屏幕上
"""