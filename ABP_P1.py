# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
print("hello world")
help('len')
# help('return')

""" 基础 form P31
注释、字面常量（Literal Constants)
数字、
字符串
单引号、双引号、三引号（“”“或''')、
"""
# P33 格式化方法
age=20
name='Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name,age))
print('Why is {0} playing with that python?'.format(name))

# P34
print('{0:.5f}'.format(1.0/3)) # 保留小数点后几位
print('{0:_^11}'.format('hello'))   # 使用…^定义字符串的长度为11位
print('{name} wrote {book}'.format(name='David',book='A Byte of python'))   # 基于关键词输出

print('aaa',end='') # 防止print不可见的换行符(\n)
print('bbb')

print('aaa',end=' ')    #指定以空格结尾
print('bbb',end=' ')
print('ccc')

# P35 转义序列（Escape Sequence）
p35str1="What's your name ?"
p35str2=""" "What's your name ?" """    #打印出双引号，空格不可少
print(p35str1,'\n',p35str2)
print(r"Newlines are indicated by \n")  #原始（Raw)字符串在前面加r或R

""" P36 变量、标识符命名规则
变量是标识符的一个例子，标识符Identifiers规则
1、首字符必须是字母或下划线
2、其它部分由字符、下划线、数字组成； #字符为ASCII或Unicode
3、区分大小写
"""
# P39 逻辑行Logical Line与物理行Physical Line
i=5;print(i)
s='This is a string. \
This continues the string.'
print(s)

# P43 运算符与表达式Expressions（运算符Operators与操作数Operands)
# 省略此部分

# P50 控制流 if 
number=23
guess=int(input('Enter an integer : '))
if guess == number:
    print('Congratulations,you guessed it.')
elif guess < number:
    print('No,it is a little highter than that')
else :
    print('No,it is a little lower than that')
print('Done')

# P53 While语句
# 省略，while 条件为真：语句（为假退出），else:（为假则可继续执行可选else块)

# P54 for循环
for i in range(1,5):
    print(i)
else:
    print('The for loop is over')





