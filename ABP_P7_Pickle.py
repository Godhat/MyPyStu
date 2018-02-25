# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
# P113 Pickle 持久化存储对象 和 Unicode
"""可通过Pickle标准模块，将任何纯Python对象存储到一个文件，
并在稍后将其取回，这叫持久化Persistently存储对象

"""
import pickle
shoplistfile='shoplist.data'
shoplist = ['apple','mango','carrot']

f = open(shoplistfile,'wb')
pickle.dump(shoplist,f)
f.close

del shoplist
f = open(shoplistfile,'rb')
storedlist = pickle.load(f)
print(storedlist)

"""
示例说明：如想将一个对象存储到文件中
1、通过open以写入write二进制binary模式打开文件
2、调用pickle模块的dump函数，此过程叫封装Pickling
3、通过pickle模块的load函数，此过程叫拆封Unpickling
"""