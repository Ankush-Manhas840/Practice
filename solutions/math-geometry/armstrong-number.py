n=1634
st=str(n)
x=n
y=0
while(x>0):
 end=x%10
 y+=end**len(st)
 x=x//10
if y==n:
  print("Armstrong")
else:
  print("Not an Armstrong")
