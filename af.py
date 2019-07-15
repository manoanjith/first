yr=int(input())
if (yr%100==0):
	if(yr%400==0):
		print('yes')
	else:
		print('no')
else:
	if (yr%4==0):
		print('yes')
	else:
		print('no')
