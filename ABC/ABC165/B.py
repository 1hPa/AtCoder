X = int(input())
A = 100
count = 0
while X > A:
  A += A // 100
  count += 1
print(count)
