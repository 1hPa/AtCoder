n = input()
num = int(n)
tmp = 0
for i in n:
  tmp += int(i)
print('Yes' if num%tmp == 0 else 'No')
