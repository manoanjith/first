a,b=input().split()
a=int(a)
b=int(b)
r=list(map(int,input().split()))[:a]
sum=0
for i in range(b):
	sum=sum+r[i]
print(sum)
