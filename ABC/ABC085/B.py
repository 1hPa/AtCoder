n=int(input())
d=[int(input()) for _ in range(n)]
d.sort()
count=0
ans=1
for i in range(n):
  if d[i-1]<d[i]:
    count+=1
print(ans+count)
