n = int(input())

for i in range(n):
  b=list(map(int,input().split()))
  
  avg = sum(b[1:])/b[0]
  c = 0
  for j in b[1:]:
    if j>avg:
      c +=1
  per = (c/b[0])*100
  print('%.3f'%per+"%")