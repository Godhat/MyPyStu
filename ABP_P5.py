# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
'''P76 数据结构Data Structures

数据结构是用来存储一系列相关数据的集合
内置有列表list、元组Tuple、字典Dictionary、集合Set
列表(List)：
1、保存有序项目的集合，用方括号表示shoplist=['apple','mango']；
2、可以添加、移除和搜索列表中的项目；
3、列表是可变Mutable的数据类型；
4、列表是使用对象与类的实例；
5、一个类有方法Method，通过点号来访问对象 mylist.append('a')
6、一个类有字段Field，只为该类定义且所用的变量，通过点号来访问mylist.field

元组(Tuple)：
1、将多个对象保存在一起,用括号表示zoo=('python','elephant','penguin');
2、元组是不可变的，不能编辑或更改元组；
3、通常用于保证某一语句或自定义的函数可以安全采用一组数值（即元组内数值不变）；
4、空元组myempty=()、一个项目元组必须加逗号singleton=(2,)

字典(Dictionary):
1、键keys与值Values唯一对应，用大括号表示d={key1:values1,key2:values2}
2、键keys只能使用不可变的对象（如字符串）；
3、值Values可使用可变和不可变的对象；
4、键值之间用冒号分隔，每一对键与值使用逗号区分；
5、字典中的键值对不会以任何方式进行排序

序列(Sequence)
列表、元组和字符串可以看作序列的表现形式，
1、序列的主要功能是资格测试Membership Test（就是in与no in表达式) \
2、和索引操作Indexing Operations，允许直接获取序列中的特定项目，如切片Slicing运算

'''
# P82 序列的切片运算 Slicing
l=[0,1,2,3,4,5,6,7,8,9]
name='David'
print('Full List is : ',l[:])
print('L[0] is : ',l[0])
print('L[1] is : ',l[1])
print('L[-1] is : ',l[-1])
print('L[-2] is : ',l[-2])
print('Name Character 0 is : ',name[0])

print()
print('List[1:3] item 1 to 3 is : ',l[1:3])
print('List[-1:] item -1 to end is : ',l[-1:])
print('List[1:-1] item 1 to -1 is : ',l[1:-1])
print('List[:-1] item no end is : ',l[:-1])
print('List[2:] item 2 to end is : ',l[2:])
print('List[:2] item start to 2 is : ',l[:2])
print('List[0:] full is : ',l[0:])

print()
print('Name Character 0 to 3 is : ',name[0:3])
print('Name Character 2 to end is : ',name[2:])
print('Name Character 2 to -1 is : ',name[2:-1])
print('Name Character start to end is : ',name[:])

"""通过索引来获取序列中的项目，也称为下标操作Subscription Operation
1、python从0开始计数，list[1]为第2个item；
2、索引操作可使用负数，从队列末尾开始，list[-1]为最后一个
3、可指定序列名称来操作，用冒号分隔，前数为切片开始位置，后数为切片结束位置
4、前数未指定则为开始处，后数未指定则为末位数
5、序列切片将包括起始位置，但不包括结束位置
6、第三个参数为切片的步长（step)，默认步长大小为1
"""
print()
print('List[::1] is full : ',l[::1])
print('List[::2] is sclicing step 2 : ',l[::2])

# P84 集合set
"""集合set是简单对象的无序集合Collection
1、当集合中的项目存在与否比起次序或其出现次数更加重要时，就使用set；
2、通过集合，可测试某些对象的资格或情况，如子集、交集
3、数学里的集合知识
"""
print()
bri=set(['Brazil','USA','Russia'])
print("USA in bri set : ",'USA' in bri)
print("India in bri set : ",'India' in bri)

bric=bri.copy()
bric.add('China')
print(bric.issuperset(bri))
bri.remove('Brazil')
print("Set bri is : ",bri)
print("Set bric is : ",bric)
print("Set bri & bric is : ",bri & bric)

# P85 引用
"""当创建一个对象并将其分配给某个变量时
1、变更只会查阅Refer某个对象；
2、它不代表对象本身；
3、变更名只是指向内存中存储了相应对象的那部分；
4、叫作名称绑定Binding给那个对象
"""

