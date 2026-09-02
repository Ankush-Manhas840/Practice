Nums = [2,-3,4,5]
pro=Nums[0]
curr_pro=Nums[0]
negat=Nums[0]
for j in range(1,len(Nums)):
  cand=Nums[j]
  cand2=curr_pro*Nums[j]
  cand3=negat*Nums[j]
  new_max = max(cand, cand2, cand3)
  new_min = min(cand, cand2, cand3)
  curr_pro=new_max
  negat=new_min
  pro=max(pro,new_max)
print(pro)
