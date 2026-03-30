n = int(input())
for i in range(n):
  a=list(input())
  total = 0
  b = 1
  for j in a:
    if j=='O':
      total+=b
      b+=1
    else:
      b = 1
  print(total)