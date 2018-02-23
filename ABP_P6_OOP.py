# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
'''P99 面向对象的编程术语

    一、面向过程(Procedure-oriented)编程方式：
       通过函数设计程序来处理数据的代码块。
    二、面向对象OOP编程方式：
        将数据与功能进行组合，将其包装在对象内。
    三、类Class:
        一个类class能创建一种新的类型Type。
    四、对象Object:
        对象object就是类的实例，如int变量就是int类的实例（对象）。
    五、字段Field:
        对象可以用属于它的普通变量来存储数据，这种属于对象/类的变量就叫字段；
        2种类型（实例变量Instance Variables、类变量Class Variables)
    六、方法Method:
        对象可以用属于类的函数来实现某些功能，这种函数叫类的方法。
    七、属性Attribute：
        字段和方法通称为类的属性。
    八、self:
        类方法比普通函数多了一个额外名字，这个名字必须添加到参数列表的开头，
        但不需要调用这个功能时为这个参数赋值，python会为它提供，这种特定的
        变更引用的是对象本身，按惯例它被赋予self名称。（相当于C++/Java/C#的this).
        例~
            假设MyClass类有myobject实例，当调用这个对象方法如
            myobject.method(arg1,arg2)时，python会自动转换成
            MyClass.method(myobject,arg1,arg2)
'''
# P100 类 Class
class Person0:
    pass
p0=Person0()  #通过类名称加一对括号，给这个类创建一个对象或实例
print(p0)

# P101 方法 Method
class Person1:
    def say_hi(self):
        print('Hello, how are you ？')
p1=Person1()
p1.say_hi()     #这2行等同于Person1().say_hi()

print()
# P102 __init__ 方法
'''__init__方法会在类的对象被实例化(Instantiated)时立即运行，
此方法对任何想进行操作的目标对象进行初始化(Initialization)操作。
'''
class Person2:
    def __init__(self,name):
        self.name=name  #name和self.name是2个变量
    def say_hi(self):
        print("Hello,My name is",self.name)
p2=Person2('David Tai') #在类下创建新的实例，采用类名加括号带参数方式
p2.say_hi()

print()
# P102 类变量与对象变量
"""P102 类变量与对象变更 术语

    1、对象的功能部分即方法；
    2、对象的数据部分即字段（绑定Bound到类到对象命名空间Namespace的普通变量；
    3、字段Field有2种类型：类变量与对象变量
    4、类变量    Class Variable
                类变量是共享Shared的，可以被该类的所有实例访问，该类变量只有
                一个副本，当此类变量改变时，所有实例中都会体现。
    5、对象变量  Objcet Variable
                对象变量由每一个独立的对象或实例拥有，每个对象都拥有属于它自己
                的字段的副本，不会被共享，也不会和其它实例的相同名称字段有关联。
"""
class Robot:
    population = 0
    def __init__(self,name):
        self.name = name
        print("(Initializing {}".format(self.name))
        Robot.population += 1
    def die(self):
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))
    def say_hi(self):
        print("Greetings,my masters call me {}.".format(self.name))
    @classmethod
    def how_many(cls):
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()