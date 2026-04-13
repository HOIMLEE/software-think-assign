m = int(input())
n = int(input())

list  = set()

for i in range(m,n+1):
  count = 0
  if i > 1 :
    for j in range(2,i):
      if i % j == 0:
        count +=1
        break
    if count == 0:
      list.add(i)


if len(list)>0:
  print(sum(list))
  print(min(list))
else:
  print(-1)
