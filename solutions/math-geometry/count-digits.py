N=0
x=str(abs(N))
print(len(x))




N=-50
if N==0:
  print(1)
else:
 count=0
 N=abs(N)
 while(N>0):
   N=N//10

   count+=1
 print(count)
