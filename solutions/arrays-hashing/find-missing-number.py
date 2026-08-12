arr=[1,2,3,5,6]
val_set=set(arr)
flag=True
for i in range(1,len(arr)+1):
  if i not in val_set:
    print(i)
    flag=False
    break


if flag:
  print("Everything is present")
print(val_set)
