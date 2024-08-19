#047 猜數字

import random
start = input('請輸入隨機數字範圍起始值：')
end = input('請輸入隨機數字範圍結束值')
start = int(start)
end = int(end)

t=0
r = random.randint(start, end)
while True:
	t += 1
	num = input('請猜數字：')
	num = int(num)
	if num == r:
		print('你猜中了！')
		print('猜了第',t,'次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('猜了第',t,'次')

