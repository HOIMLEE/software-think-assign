a = int(input())
b = list(map(int,input().split()))
r= 0

for i in range (a):
  for j in range(i+1,a):
    r += abs(b[i]-b[j])
print(r*2)
