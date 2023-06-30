'''
GB 11643 公民身份号码生成器（仅供学习使用）
This Python file is edited by Misaka10072
Last modified: 2023/6/30
GitHub: https://github.com/sjzyQwQ/PyTools
'''
import random
import datetime

a=['1','0','X','9','8','7','6','5','4','3','2']

while True:
    GB2260 = int(input("请输入6位数字地址码（符合GB 2260规范，本程序将不会检验本数字是否正确，请自行确认）："))
    if GB2260 >= 100000 and GB2260 < 830000:
        break

year = random.randint(1970, datetime.datetime.today().year)
month = random.randint(1, 12)
if month < 8 and month != 2:
    day = random.randint(1, 31 if month % 2 else 30)
elif month > 7:
    day = random.randint(1, 30 if month % 2 else 31)
else:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        day = random.randint(1, 29)
    else:
        day = random.randint(1, 28)

Sequential_code = random.randint(1, 999)

GB11643 = str(GB2260) + str(year) + (str(month) if month > 9 else '0' + str(month)) + (str(day) if day > 9 else '0' + str(day))
if Sequential_code < 10:
    GB11643 += '00' + str(Sequential_code)
elif Sequential_code < 100:
    GB11643 += '0' + str(Sequential_code)
else:
    GB11643 += str(Sequential_code)

MOD11=(GB2260//100000*7+GB2260//10000%10*9+GB2260//1000%10*10+GB2260//100%10*5+GB2260//10%10*8+GB2260%10*4\
    +year//1000*2+year//100%10*1+year//10%10*6+year%10*3\
    +month//10*7+month%10*9\
    +day//10*10+day%10*5\
    +Sequential_code//100*8+Sequential_code//10%10*4+Sequential_code%10*2)%11

print(GB11643+a[MOD11])