# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
# P113 Pickle 持久化存储对象
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