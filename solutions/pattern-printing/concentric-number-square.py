n=6
num=n
for x in range(1,n*2):
  for y in range(1,n*2):
    top=x-1
    bottom=n*2-1-x
    left=y-1
    right=n*2-1-y
    print(n-min(top,bottom,left,right),end="")

  print()
