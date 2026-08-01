def rev(st,front,end):
  if(front>=end):
    print("Palindrome")
    return

  elif(st[front]!=st[end]):
      print("Not a Palindrome")
      return
  else:
   return rev(st,front+1,end-1)


st="ABCD"
rev(st,0,len(st)-1)
