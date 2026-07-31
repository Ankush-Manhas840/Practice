n=1000
result=[]
i=1
while(i*i<=n):
  if n%i==0:
    result.append(i)
    if i*i!=n:
      result.append(n//i)
  i+=1
print(result)
