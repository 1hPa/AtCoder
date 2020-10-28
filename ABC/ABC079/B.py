n=int(input())
lis=[2,1]
for i in range(n):
  lis.append(lis[i]+lis[i+1])
print(lis[n])
