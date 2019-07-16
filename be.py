st,en=input().split()
st=int(st)
en=int(en)
for i in range(st+1,en):
	count=0
	for x in range(1,i+1):
		if(i%x==0):
			count+=1
	if(count==2):
		print(i,end=' ')
