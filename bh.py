st,en=input().split()
st=int(st)
en=int(en)
for i in range(st+1,en):
	sum=0
	tem=i
	while tem>0:
		sum+=(tem%10)**3
		tem//=10
	if i==sum:
		print(i,end=" ")
