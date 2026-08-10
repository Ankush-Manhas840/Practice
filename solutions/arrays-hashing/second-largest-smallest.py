def checker(arr):
 small=float('inf')
 large=float('-inf')

 small2=float('inf')
 large2=float('-inf')
 for i in range(len(arr)):
   if arr[i]>large:
     large2=large

     large=arr[i]
   if arr[i]>large2 and arr[i]<large:
     large2=arr[i]
   if arr[i]<small:
     small2=small
     small=arr[i]
   if small2>arr[i] and arr[i]>small:
     small2=arr[i]
 return large, large2, small, small2
