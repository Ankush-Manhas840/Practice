def next_row(prearr):
  new=[1]
  for i in range(len(prearr)-1):
    new.append(prearr[i]+prearr[i+1])

  new.append(1)
  return new

N=5
c=3
ret=[1]
for y in range(1,N):

  ret=next_row(ret)

print(ret[c-1])
