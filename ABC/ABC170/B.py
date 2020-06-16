x, y = map(int, input().split())
turtle = x*4
crane = x*2
if y%2!=0:
  print('No')
elif crane<=y<=turtle:
  print('Yes')
else:
  print('No')
