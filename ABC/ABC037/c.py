n, k = map(int, input().split())
a = list(map(int, input().split()))
A = sum(a[:k])
ans = A
for i in range(n-k):
  A +=  a[k+i] - a[i]
  ans += A
print(ans)
