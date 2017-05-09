# -*- coding: UTF-8 -*-
'''1.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'''
count = 0
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if i != j and i != k and j != k:
				count += 1
				print (i, j, k)
print ('总共有%d个' %count)
print ('====================separate line====================')

'''2.企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
	利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元
	的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
	40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于
	60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
	从键盘输入当月利润I，求应发放奖金总数？'''
#method 1
'''def calculate_bonus (profit):
	if 0 <= profit <= 10:
		return profit * 0.1
	elif 10 < profit <= 20:
		return 10 * 0.1 + (profit - 10) * 0.075
	elif 20 < profit <= 40:
		return 10 * 0.1 + 10 * 0.075 * (profit - 20) * 0.05
	elif 40 < profit <= 60:
		return 10 * 0.1 + 10 * 0.075 + 20 * 0.005+ (profit - 40) * 0.03
	elif 60 < profit <= 100:
		return 10 * 0.1 + 10 * 0.075 + 20 * 0.005 + 20 * 0.003 + (profit - 60) * 0.015
	elif profit >= 100:
		return 10 * 0.1 + 10 * 0.075 + 20 * 0.005 + 20 * 0.003 + 40 * 10.0015 (profit - 100) * 0.01
	else:
		print ('输入错误')
print ('应发放奖金总数%.2f万元' %(calculate_bonus(float(input('当月利润：')))))'''

#method 2
profit = float(input('当月利润：'))
levels = [100, 60, 40, 20, 10, 0]
rates = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
bonus = 0.0
for idx in range(0, 6):
	if profit > levels[idx]:
		bonus += (profit - levels[idx]) * rates[idx]
		profit = levels[idx]

print ('应发放奖金总数%.2f万元' %bonus)
print ('====================separate line====================')

'''3.一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？'''
# x + 100 = m * m
# x + 100 + 168 = n * n
# n * n - m * m = 168
# (n + m) * (n - m) = 168
# i = n + m, j = n - m, i * j = 168
# n = (i + j) / 2, m = (i - j) / 2
# i * j = 168, j >= 2 ====> 1 < i < 168 / 2 + 1

for i in range(1, 85):
	if 168 % i == 0:	#i和j均能被整除
		j = 168 / i
		if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
			n = (i + j) / 2
			m = (i - j) / 2
			x = m * m - 100
			print (int(x))
print ('====================separate line====================')

'''4.输入某年某月某日，判断这一天是这一年的第几天？'''
year = int(input('请输入年份：'))
month = int(input('请输入月份：'))
day = int(input('请输入日子：'))

def order_of_year(year, month, day):
	months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

	order = 0
	#闰年判定方法：能被400整除。或者能被4整除但不能被100整除。
	isLeepYear = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
	if 0 < day <= 31:
		if (month == 2 and isLeepYear and day > 29) or (month == 2 and (not isLeepYear) and day > 28):
			print ('输入的日子不合适')
		else:
			order += day
			#计算之前的月份天数
			if 0 < month <= 12:
				order += months[month - 1]

				if isLeepYear and month > 2:
					order += 1
				print ('%d 年 %d 月 %d 日是 %d 年的第 %d 天' %(year, month, day, year, order))
			else:
				print ('输入的月份不合适')
	else:
		print ('输入的日子不合适')

order_of_year(year, month, day)

'''5.输入三个整数x,y,z，请把这三个数由小到大输出。'''
x = int(input('x:'))
y = int(input('y:'))
z = int(input('z:'))

list1 = [x, y ,z]
list1.sort()

print (list1)

'''6.斐波那契数列。'''
def fibonacci_sequence(n):	#n表示多少以内
	a = 0
	b = 1
	while b < n:
		a, b = b, a + b
		print(a)

fibonacci_sequence(100)