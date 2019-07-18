st=input()
co=0
for i in st:
	if (i.isdigit() or i.isalpha() or i==' '):
		co=co
	else:
		co+=1
print(co)
