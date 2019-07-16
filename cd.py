n=int(input())
a=list(map(int,input().split()))[:n]
a.sort()
for i in range(n):
	print(a[i],end=' ')
