#047 猜數字

import random
t=0
r = random.randint(1, 100)
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
		print('猜了第',t,'次')
	elif num < r:
		print('比答案小')
		print('猜了第',t,'次')

