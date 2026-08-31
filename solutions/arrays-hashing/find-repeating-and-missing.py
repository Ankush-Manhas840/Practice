arr=[1,2,2,4]
s1=0
s2=0
sum_no=0
sum_ab=0
squar_no=0
squar_ab=0
for i in range(0,len(arr)):
  sum_no+=(i+1)
  sum_ab+=arr[i]
  squar_no+=(i+1)**2
  squar_ab+=arr[i]**2

s1=sum_ab-sum_no
s2=squar_ab-squar_no


a=int((s1**2+s2)/(2*s1))
b=a-s1
print(a,b)
