def primenumber(Num):
  n = 0
  i = 2
  for i in range(2,Num//2+1):
    if Num % i == 0:
      n = n + 1
      break
  if n == 0:
    print(Num, end=" ")

x = 10
print("Prime numbers less than", x, "are:")
for i in range(2, x+1):
  primenumber(i)