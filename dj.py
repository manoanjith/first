st=int(input())
a=0
b=1
c=1
for i in range(st):
	print(c,end=' ')
	c=a+b
	a=b
	b=c
