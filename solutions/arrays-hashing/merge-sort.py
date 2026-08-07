def merge(left,right):
  result=[]
  i=0
  j=0
  while i!=len(left) and j!=len(right):
    if left[i]>=right[j]:
      result.append(right[j])
      j+=1
    else:
      result.append(left[i])
      i+=1

  result.extend(right[j:])

  result.extend(left[i:])
  return result


def merge_sort(arr):
  if len(arr)==1:
    return arr
  mid=len(arr)//2
  left=merge_sort(arr[:mid])
  right=merge_sort(arr[mid:])
  return merge(left,right)


arr=[2,1,3]
merge_sort(arr)
