# 產生一個隨機整數1～100（不要印出來）
# 讓使用者去猜數子
# 猜對要說 "終於猜對"
# 猜錯要說比答案大/小

import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1
	g = input('請猜數字: ')
	g = int(g)
	if r == g:
		print('終於猜對了!')
		print('這是你猜的第', count, '次')
		break
	elif r > g:
		print('比答案小！')
	else:
		print('比答案大！')
	print('這是你猜的第', count, '次')
