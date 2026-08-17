arr=[-2, -3, -5, -2,- 7, -4]
sum=float('-inf')
curr_sum=0

for x in arr:


  if(curr_sum<=0):
    curr_sum=0



  curr_sum+=x

  sum=max(sum,curr_sum)



print(sum)
