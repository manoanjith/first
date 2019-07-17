st=int(input())
a=(list(map(int,input().split())))[:st]
for i in range(st):
	for x in range(st):
		if(a[i]<a[x]):
			temp=a[i]
			a[i]=a[x]
			a[x]=temp

for i in range(st):
	print(a[i],end=' ')
