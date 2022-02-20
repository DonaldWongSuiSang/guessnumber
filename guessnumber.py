# 產生一個隨機整數1～100（不要印出來）
# 讓使用者去猜數子
# 猜對要說 "終於猜對"
# 猜錯要說比答案大/小

import random

r = random.randint(1, 100)
while True:
	g = input('請猜數字: ')
	g = int(g)
	if r == g:
		print('終於猜對了!')
		break
	else:
		if r > g:
			print('比答案小！')
		else:
			print('比答案大！')
