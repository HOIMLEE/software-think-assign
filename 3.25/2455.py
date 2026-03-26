a, b = map(int,input().split())
c, d = map(int,input().split())
e, f = map(int,input().split())
g, h = map(int,input().split())


first = b

second = b - c + d

third = second - e + f

if first > second and first>third:
  print(first)
elif second>first and second>third:
  print(second)
else:
  print(third)
