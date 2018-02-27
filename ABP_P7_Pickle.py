# encoding=utf-8
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

# P114 Unicode
"""Unicode类型以字母u开头，如u"hello world"
将Unicode字符串转换至一个能够被发送和接收的格式，这格式叫UTF-8,
这种格式可以进行读取和写入，只需要使用关键字参数到标准open函数中
"""
ustr1="hello,english words!"
ustr2=u"您好,unicode words!"
print("ustr1 is : ",ustr1,type(ustr1))
print("ustr2 is : ",ustr2,type(ustr2))


import io
f = io.open("abc.txt","wt",encoding="utf-8")
f.write(u"Imagine non-English language here..")
f.close
text=io.open("abc.txt",encoding="utf-8").read()
print("open text is :",text)   #ERROR 实际显示不出text内容，可能函数版本

"""
io.open提供了编码Encoding和解码Decoding参数来使用Unicode
"""