# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
'''P125 More 更多其它python知识

    传递元组，特殊方法，单语句块，Lambda表格，
    列表推导，在函数中接收元组与字典，assert语句，
    装饰器，python2与python3的不同，迈出下一步
'''
# 传递元组：使用一个元组从一个函数中返回2个不同的值
def get_error_details():
    return(2,'details')
errnum,errstr=get_error_details()
print("ErrorNumber is {0} ; String is '{1}' "
      .format(errnum,errstr))

def prt(a,b):
    print("a is {0} ; b is {1} .".format(a,b))

a=5;b=8
prt(a,b)
a,b=b,a #交换2个变量的快速方法
prt(a,b)

# 特殊方法
