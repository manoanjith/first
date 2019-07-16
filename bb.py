n1=int(input())
rev=0
n2=n1
while n1>0:
  rev=(rev*10)+n1%10
  n1=n1/10
if rev==n2:
  print('yes')
els
  print('no')
