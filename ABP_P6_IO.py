# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
'''P110 输入与输出
    
    1、输入与输出
    2、文件
'''
# P110 用户输入内容
def reverse(text):
    return text[::-1]
def is_palinrome(text):
    return text == reverse(text)    #判定是不是回文

something = input("Enter text : ")
if is_palinrome(something):
    print("Yes,it is a palindrome")
else:
    print("No,it is not a palindrome.")

# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
'''P76 数据结构Data Structures
