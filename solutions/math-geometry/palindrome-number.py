n=77877
x=n
y=0

while(x>0):
  y*=10
  y+=x%10

  x=x//10
print(y)
if(y==n):
  print("Palindrome")
else:
  print("Not a Palindrome")
