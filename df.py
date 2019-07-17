stin=input()
count=0
for i in stin:
	if (i.isdigit() or i.isalpha() or i==' '):
		cont=count
	else:
		count+=1
print(count)
