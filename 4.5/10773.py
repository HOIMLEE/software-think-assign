k = int(input())
b=[]
t=[]
for i in range(k):
  b.append(int(input()))
for j in b:
  if j != 0:
    t.append(int(j))
  else:
    t.pop()
print(sum(t))
