# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
'''P111 文件
'''
peom='''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use python!!
'''

f = open('poem.txt','w')
f.write(peom)
f.close

f = open('poem.txt') #默认以'r'ead模式
while True:
    line=f.readline()
    if len(line) == 0:
        break
    print(line,end='')

f.close

# P113 Pickle 持久化存储对象
"""可通过Pickle标准模块，将任何纯Python对象存储到一个文件，
并在稍后将其取回，这叫持久化Persistently存储对象

"""
import