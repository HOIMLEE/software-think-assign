t = int(input())
for i in range(t):
  a = input()
  while a.find("()") != -1:
    a = a.replace('()','')
  
  if a == '': print("YES")
  else: print("NO")