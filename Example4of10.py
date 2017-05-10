# -*- coding: UTF-8 -*-
'''31.请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。'''
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
str1 = input('请输入第一个字母：')
if str1 == 'T' or str1 == 'S':
	str2 = input('请输入第二个字母：')
	if str2 == 'h':
		print ('Thursday -- 星期四')
	elif str2 == 'a':
		print ('Saturday -- 星期六')
	elif str1 == 'T' and str2 == 'u':
		print ('Tuesday -- 星期二')
	elif str1 == 'S' and str2 == 'u':
		print ('Sunday -- 星期日')
	else:
		print ('input error.')
elif str1 == 'M':
	print ('Monday -- 星期一')
elif str1 == 'W':
	print ('Wednesday -- 星期三')
elif str1 == 'F':
	print ('Friday -- 星期五')
else:
	print ('input error.')
print ('====================separate line====================')

'''32.按相反的顺序输出列表的值。'''
list1 = ['P', 'y', 't', 'h', 'o', 'n']
list2 = list1[:]
list2.reverse()
print (list1, list2)
print ('====================separate line====================')

'''33.按逗号分隔列表。'''
list3 = ['H', 'e', 'l', 'l', 'o']
for c in list3:
	if c == list3[-1]:
		print(c)
	else: 
		print ('%s,' %c, end = '')
print ('====================separate line====================')

'''34.练习函数调用。'''
def fun1(n):
	return fun2(n) + 1
def fun2(n):
	return n ** 3
print (fun1(3))
print ('====================separate line====================')

'''35.文本颜色设置。'''
# 终端的字符颜色是用转义序列控制的，是文本模式下的系统显示功能，和具体的语言无关。
# 转义序列是以ESC开头,即用\033来完成（ESC的ASCII码用十进制表示是27，用八进制表示就是033）。
# 格式：\033[显示方式;前景色;背景色m
'''
\33[0m 关闭所有属性 
\33[1m 设置高亮度 
\33[4m 下划线 
\33[5m 闪烁 
\33[7m 反显 
\33[8m 消隐 
\33[30m -- \33[37m 设置前景色 
字颜色:30-----------37 
30:黑 
31:红 
32:绿 
33:黄 
34:蓝色 
35:紫色 
36:深绿 
37:白色 
\33[40m -- \33[47m 设置背景色 
字背景颜色范围:40----47 
40:黑 
41:深红 
42:绿 
43:黄色 
44:蓝色 
45:紫色 
46:深绿 
47:白色 
\33[90m -- \33[97m 黑底彩色 
90:黑 
91:深红 
92:绿 
93:黄色 
94:蓝色 
95:紫色 
96:深绿 
97:白色 
\33[nA 光标上移n行 
\33[nB 光标下移n行 
\33[nC 光标右移n行 
\33[nD 光标左移n行 
\33[y;xH设置光标位置 
\33[2J 清屏 
\33[K 清除从光标到行尾的内容 
\33[s 保存光标位置 
\33[u 恢复光标位置 
\33[?25l 隐藏光标 
\33[?25h 显示光标 
'''
print ('\033[5;97m' + 'hey man')
print ('\033[0m')	#恢复默认
print ('====================separate line====================')

'''36.求100之内的素数。'''
def is_prime(n):
	for x in range(2, n):
		if n % x == 0:
			return False
	return True

for x in range(2, 101):
	if is_prime(x):
		print (x)
print ('====================separate line====================')

'''37.对10个数进行排序。'''
import random as r

list1 = []
for x in range(0, 10):
	list1.append(r.randint(10, 100))
print (list1)
list1.sort()
print (list1)
print ('====================separate line====================')

'''38.求一个3*3矩阵对角线元素之和。'''
list2 = []
for i in range(0, 3):
	list2.append([])
	for j in range(0, 3):
		list2[i].append(r.randint(10, 100))
print (list2)

sum = 0
for x in range(0, 3):
	sum += list2[x][x]
print ('sum =', sum)
print ('====================separate line====================')

'''39.有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。'''
list3 = [1, 3, 5, 6, 8, 10, 15, 23, 42, 68]
intputNum = int(input('请输入:'))
def insert_index(intputNum, list, low, high):
	mid = (low + high) // 2
	print (low, mid, high)
	if low < high:
		if high - low == 1 or high - low == 2:
			return mid
		if list3[mid] > intputNum:
			return insert_index(intputNum, list3, low, mid)
		else:
			return insert_index(intputNum, list3, mid + 1, high)
idx = insert_index(intputNum, list3, 0, len(list3))

if idx + 1 < len(list3):
	if intputNum <= list3[idx - 1]:
		idx -= 1
	# elif list3[idx - 1] < intputNum <= list3[idx]:

	elif list3[idx] <= intputNum < list3[idx + 1]:
		idx += 1
	elif intputNum >= list3[idx + 1]:
		idx += 2
else:
	if intputNum > list3[-1]:
		idx += 1

list3.insert(idx, intputNum)
print (list3)
print ('====================separate line====================')

'''40.将一个数组逆序输出。'''
list4 = []
for x in range(5):
	list4.append(r.randint(10, 100))
print (list4, list4[::-1])