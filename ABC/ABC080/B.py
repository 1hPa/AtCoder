N = input()
N_1 = int(N)
S = sum(map(int, list(N)))
if N_1 % S == 0:
  print("Yes")
else:
  print("No")
