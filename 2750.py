n=int(input())
a = []
for i in range(n):
  a.append(int(input()))

b=list(sorted(a))

for j in range(0,n,1):
  print(b[j])
