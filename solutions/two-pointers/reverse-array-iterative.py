a=[1,2,3,4,5,6]
j=1
for i in range(len(a)//2):
  temp=a[-j]
  a[-j]=a[i]
  a[i]=temp
  j+=1
print(a)
