# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
# P58 函数functions
def say_hello():
    print('Hello world')

say_hello()
say_hello()

# P59 函数参数
"""在定义函数时给定的名称称为形参Parameters，
在调用函数时所提供给函数的值称为实参Arguments
"""
def print_max(a,b):
    if a>b:
        print(a,'is Maximum')
    elif a==b:
        print(a,'is equal to',b)
    else :
        print(b,'is Maximum')

print_max(10, 13) #直接传递字面值
x=5
y=7
print_max(x, y) #以参数形式传递变量

# P60 局部变量 local,作用域 Scope
xx=50
def func(xx):
    print('xx is',xx)
    xx=2    #函数的局部变量
    print('Change local xx to',xx)

func(xx)
print('xx is still',xx) #主代码块的变量

# P61 global 全局变量（避免使用）
print()
yy=50
def funcy():
    global yy   #声明yy是一个全局变量，将改动主代码块的yy值
    print('yy is',yy)
    yy=2
    print('Changed global yy to ',yy)

funcy()
print('Value of yy is :',yy)

# P62 默认参数值,只有位置参数列表末尾的参数才能有此值
def say(message,times=1):
    print(message*times)

say('Hello！ ')
say('World ! ',5)

print()
# P63 关键字参数 Keyword Arguments
"""1、不需要考虑参数的顺序
2、只对希望赋值的参数赋值，其它使用默认值
"""
def funcka(a,b=5,c=10):
    print('a is: ',a,' and b is: ',b,\
          ' and c is: ',c)
funcka(3,7)
funcka(25,c=24)
funcka(c=50,a=100)

print()
# P63 可变参数，定义的函数里面能够有任意数量的变量
"""参数数量是可变的，通过星号来实现
*param星号参数，从此处开始到结束所有位置参数都汇集为一个名为param的无组(Tuple)
**param双星号参数，所有关键字参数都汇集为一个名为param的字典（Dictionary)
"""
def total(a=5,*number,**phonebook):
    print('a',a)
    for single_item in number:
        print('single_item ' ,single_item)
    for first_part,second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,Jack=1123,john=2231,Inge=1560))

print()
# P64 return语句，用于从函数中返回，也是中断函数
"""每个函数末尾隐含了一句return None，None在Python中是个特殊类型，代表虚无
pass语句用于指示一个没有内容的语句块
"""
def maximum(x,y):
    if x>y:
        return x
    elif x==y:
        return 'the numbers are equal.'
    else:
        return y
print(maximum(2, 3))

print()
# P65 DocStrings，文档字符串Documentation Strings
def print_max(xxx,yyy):
    '''Prints the maximum of two numbers.
    
    The two values must be integers.'''
    xxx=int(xxx)
    yyy=int(yyy)
    if xxx>yyy:
        print(xxx,'is maximum')
    else:
        print(yyy,'is maximum')
print_max(3,5)
"""
函数第一行逻辑行中的字符串是该函数的文档字符串DocSting，约定为
是一串多行字符串；
第一行首字母大写，以句号结束；
第二行为空行；
第三行为解释说明。
        可通过使用函数的__doc__属性来获取，help()和pydoc命令可使用文档字符串

"""
print(print_max.__doc__)