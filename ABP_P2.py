# Godhat Study from <<A Byte of Python>>
# Version 4.06c  public 2017-07-28
# P54 for循环
for i in range(1,5):
    print(i)
else:
    print('The for loop is over')

for j in range(0,10,2):print(j)
print(list(range(0,10,2)))
print(list(range(10)))

# P55 break语句，直接中断循环语句的执行，及包括else块
# P56 continue语句，跳过当前循环中的剩余语句，继续下一次迭代
while True:
    s=input('Enter something :')
    if s=='quit':
        break
    if len(s)<3:
        print('Too small')
        continue
    print('Input is of sufficient length')