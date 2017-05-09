# -*- coding: UTF-8 -*-
'''11.古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
	小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？'''
#1------------1
#2------------1
#3------------2
#4------------3
#5------------5
#6------------8
#研究规律发现还是斐波那契数列
month = int(input('输入几个月后：'))
def total_count(month):
	if month == 1 or month == 2:
		return 1
	else:
		return total_count(month - 2) + total_count(month - 1)
print ('第 %d 个月兔子总数为 %d 只' %(month, total_count(month) * 2))
print ('====================separate line====================')

'''12.判断101-200之间有多少个素数，并输出所有素数。'''
#定义判断是否为素数的函数
def prime(x):
	for i in range(2, x):
		if x % i == 0:
			return False
	return True
	
for x in range(101, 201):
	if prime(x):
		print (x)
print ('====================separate line====================')

'''13.打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
	其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，
	因为153=1的三次方＋5的三次方＋3的三次方。'''
def narcissistic_num(x):
	if x < 100 or x > 999:
		return False
	else:
		i = x // 100
		j = (x // 10) % 10
		k = x % 10
		if i ** 3 + j ** 3 + k ** 3 == x:
			return True
		return False
for x in range(100,1000):
	if narcissistic_num(x):
		print (x)
print ('====================separate line====================')

'''14.将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。'''
# 90 = 2 * 45
# 90 = 2 * 3 * 15
# 90 = 2 * 3 * 3 * 5
oriNum = int(input('请输入一个正整数：'))
list1 = []

num = oriNum
temp = 2
if prime(num):
	list1.append(1)
	list1.append(num)
else:
	while temp < num:
		if num % temp == 0:
			list1.append(temp)
			num //= temp
			#判断num是否是素数
			if prime(num):
				list1.append(num)
		else:
			temp += 1

print ('%d=' %oriNum, end = '')

idx = 0
for item in list1:
	if idx == len(list1) - 1:
		print ('%d' %item)
	else:
		print ('%d*' %item,  end = '')
	idx += 1
print ('====================separate line====================')

'''15.利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。'''
score = int(input('请输入成绩：'))
if score > 100 or score < 0:
	print ('输入错误❎')
else:
	if score >= 90:
		print ('评分：A')
	elif 60 <= score <= 89:
		print ('评分：B')
	else:
		print ('评分：C')
print ('====================separate line====================')

'''16.输出指定格式的日期。'''
import time as t

formatTime = t.strftime('%Y-%m-%d %H:%M:%S', t.localtime())
print (formatTime, type(formatTime))
print ('====================separate line====================')

'''17.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。'''
stringInput = input('请输入一行字符：')
letters = 0
spaces = 0
digits = 0
others = 0
for x in stringInput:
	if x.isalpha():
		letters += 1
	elif x.isspace():
		spaces += 1
	elif x.isdigit():
		digits += 1
	else:
		others += 1
print ('%s :letters:%d\tspaces:%d\tdigits:%d\tothers:%d' %(stringInput, letters, spaces, digits, others))
print ('====================separate line====================')

'''18.求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
	例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。'''
rawNum = int(input('请输入10以内的正整数：'))
n = int(input('相加次数：'))
def cal(rawNum, n):
	next = 0
	total = 0
	list2 = []
	for i in range(0, n):
		next += (10 ** i) * rawNum
		list2.append(next)
	for item in list2:
		total += item
	return total
print ('total:', cal(rawNum, n))
print ('====================separate line====================')

'''19.一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。'''
for i in range(1, 1001):
	sum = 0
	for j in range(1, i):
		if i % j == 0:
			sum += j
	if sum == i:
		print(i)
print ('====================separate line====================')

'''20.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？'''
height = 100
def latest_height(n):
	return 100 * (0.5 ** n)
def total_height(n):
	totalHeight = 100							#第一次是单程
	for x in range(1, n):
		totalHeight += 100 * (0.5 ** x) * 2		#后面都是弹起和下落双程
	return totalHeight

print ('第10次落地时经过 %.6f 米，第10次反弹 %.6f 米' %(total_height(10), latest_height(10)))