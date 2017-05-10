# -*- coding: UTF-8 -*-
'''21.猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，
	又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后
	每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只
	剩下一个桃子了。求第一天共摘了多少。'''
total = 1
for day in range(0, 9):
	total = (total + 1) * 2
print ('第一天共摘了%d个桃子' %total)
print ('====================separate line====================')

'''22.两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
	已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和
	x,z比，请编程序找出三队赛手的名单。'''
# c ---> y
# a ---> z
# b ---> x
team1 = ['a', 'b', 'c']
team2 = ['x', 'y', 'z']

for a in team2:
	for b in team2:
		for c in team2:
			if a != b and b != c and a != c and a != 'x' and c != 'x' and c != 'z':
				print ('a ----> %s b ----> %s c ----> %s' %(a, b, c))
print ('====================separate line====================')

'''23.打印出菱形'''
def print_diamond(n):	#n为层数 （奇数）
	m = n // 2
	for x in range(0, m + 1):
		print (' ' * (m - x) + '*' * (2 * x + 1))
	for x in range(0, m):
		print (' ' * (x + 1) + '*' * ((m - x) * 2 - 1))
print_diamond(3)
print ('====================separate line====================')

'''24.有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。'''
a = 2.0
b = 1.0
total = 0.0

for x in range(0, 20):
	total += a / b
	b, a = a, a + b		#不能写作 b = a    a = a + b 因为此时b的值已经改变
	# print (a, b)

print ('total:%.4f' %total)
print ('====================separate line====================')

'''25.求1+2!+3!+...+20!的和。'''
def factorial(n):
	num = 1
	for x in range(1, n + 1):
		num *= x
	return num

sum = 0
for x in range(1, 21):
	sum += factorial(x)

print ('1! + 2! + 3! + ... + 20! =', sum)
print ('====================separate line====================')

'''26.利用递归方法求5!。'''
def fun1(n):
	if n == 0 or n == 1:
		return 1
	return n * fun1(n - 1)

print ('5! =', fun1(5))
print ('====================separate line====================')

'''27.利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。'''
str1 = input('请输入字符：')
list1 = list(str1)
list1.reverse()
for c in list1:
	print(c)
print ('====================separate line====================')

'''28.有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，
	他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个
	人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？'''
age = 10
for person in range(1, 5):
	age += 2
print ('第5个人%d岁' %age)
print ('====================separate line====================')

'''29.给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。'''
str2 = input('请输入正整数：')
print('这是一个%d位数' %(len(str2)))
idx = 0
for c in str2:
	print(str2[len(str2) - idx - 1])
	idx += 1
print ('====================separate line====================')

'''30.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。'''
num = int(input('请输入5位数：'))
def judge_palindrome_number(num):
	# x = num // 10000	#万位
	# y = num % 10000 // 1000	#千位
	# z = num % 1000 % 1000 // 100	#百位
	# m = num % 1000 % 1000 % 100 // 10	#十位
	# n = num % 1000 % 1000 % 100 % 10	#个位
	str3 = str(num)
	for x in range(0, len(str3) // 2):
		if str3[x] != str3[len(str3) - x - 1]:
			return False
	return True

print ('%d 是否是回文数：' %num, judge_palindrome_number(num))