nums=[7, 0, 0, 1, 7, 7, 2, 7, 7]

hashmap=dict()
for x in range(len(nums)):
  hashmap[nums[x]]=hashmap.get(nums[x],0)+1



for key,value in hashmap.items():
  if value>=len(nums)//2:
    print(key)
