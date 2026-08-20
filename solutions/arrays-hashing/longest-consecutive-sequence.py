arr=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

setz=set(arr)
best=0
for start in setz:
  x=start
  length=1

  while(x+1  in setz):
    x+=1
    length+=1
  best=max(length,best)


print(best)
