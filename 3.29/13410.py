a, b = map(int,input().split())

num = []
for i in range (1,b+1):
  num.append(int(str(a*i)[::-1]))
print(max(num))
