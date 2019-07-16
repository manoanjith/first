st=int(input())
fact=1
if st==0:
	print(fact)
else:
	for i in range(1,st+1):
		fact*=i
	print(fact)
