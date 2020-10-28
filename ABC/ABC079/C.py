a2d=input()
for i in range(1<<3):
  total=int(a2d[0])
  f=a2d[0]
  for j in range(3):
    if i&(1<<j):
      total+=int(a2d[j+1])
      f+='+'
    else:
      total-=int(a2d[j+1])
      f+='-'
    f+=a2d[j+1]

  if total==7:
    print(f+'=7')
    exit()
