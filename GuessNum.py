# -*- encoding: UTF-8 -*-

#获取一个 1-100 的随机数	目标值
import random
goalNum = random.randint(1,100)
print('目标值：', goalNum)

num = -1
while num != goalNum:
	num = int(input('请输入1-100内的随机数：'))
	if num > goalNum:
		print('大了')
	elif num < goalNum:
		print('小了')

print('Congratulations!')
