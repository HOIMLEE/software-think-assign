a, b, c= map(int,input().split())
d = int(input())

s = (c+d)%60

m = (b+((c+d)//60))%60

h = (a+(b+((c+d)//60))//60)%24

print(h,m,s)