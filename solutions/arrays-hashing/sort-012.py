nums = [1,1,1,2,0,0,0,2,2]

hashmap=dict()
for x in nums:
  hashmap[x]=hashmap.get(x,0)+1



zero=hashmap.get(0,0)
one=hashmap.get(1,0)
two=hashmap.get(2,0)
nums[0:zero]=[0]*zero
nums[zero:one+zero]=[1]*one
nums[one+zero:one+zero+two]=[2]*two

print(nums)
