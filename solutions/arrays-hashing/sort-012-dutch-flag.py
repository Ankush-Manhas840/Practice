nums = [1,1,1,2,0,0,0,2,2]

low=0
high=len(nums)-1
mid=0

while(mid<=high):
  if nums[mid]==0:
    temp=nums[low]
    nums[low]=nums[mid]
    nums[mid]=temp
    low+=1

  elif nums[mid]==1:
    mid+=1

  elif nums[mid]==2:
    temp=nums[mid]
    nums[mid]=nums[high]
    nums[high]=temp
    high-=1



print(nums)
