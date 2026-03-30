n = int(input())

a = list(map(int,input().split()))

b = a[:n]
print(min(b) ,max(b))