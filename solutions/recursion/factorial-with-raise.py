def fact(n):
  if(n<0):
   raise ValueError("Undefined")

  if n==1 or n==0:
    return 1
  else:
    return fact(n-1)*n

x=fact(-2)
print(x)
