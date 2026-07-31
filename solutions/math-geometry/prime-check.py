n=97
i=2
count=True
while(i*i<=n):
  if(n%i==0):
    count=False
    print("Not a PRIME")
    break
  i+=1
if(count):
  print("Prime")
