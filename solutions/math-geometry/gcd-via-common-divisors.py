def divi(x):
  lio=[]
  for i in range(1,x+1):
    if x%i==0:
      lio.append(i)
  return lio

x=20
y=15
re1=divi(x)
re2=divi(y)
#print(re2)
#print(re1)
common=[]
for i in  re2:
  if i in re1:
    common.append(i)
print(max(common))
