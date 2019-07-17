st=int(input())
b=(list(map(int,input().split())))[:st]
for i in range(st):
	print(b[i],b.index(b[i]))
