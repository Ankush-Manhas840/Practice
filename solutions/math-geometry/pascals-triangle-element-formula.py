r=5
c=3
prev=1
r-=1
for i in range(1,c):
  prev=prev*(r/i)
  r-=1

print(int(prev))
