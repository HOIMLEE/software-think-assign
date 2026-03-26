for _ in range(3):
  a = list(map(int, input().split()))
  if sum(a) == 4:
    print("E")
  elif sum(a)==0:
    print("D")
  elif sum(a)==1:
    print("C")
  elif sum(a)==2:
    print("B")
  else:
    print("A")
