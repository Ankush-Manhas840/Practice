def fibo(n):
  if n==1 or n==0:
    return 1
  else:
    return  fibo(n-1)+fibo(n-2)


n=5
print(fibo(n))
