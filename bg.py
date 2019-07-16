no=int(input())
sum=0
tem=no
while tem>0:
	sum+=(tem%10)**3
	tem//=10
if no==sum:
	print('yes')
else:
	print('no')
