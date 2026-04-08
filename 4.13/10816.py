m = int(input())
num = list(map(int,input().split()))
n_dict = {}
for i in num:
  if i not in n_dict:
    n_dict[i] = 1
  else:
    n_dict[i] +=1

M = int(input())
M_list = list(map(int,input().split()))
result = []

for j in M_list:
  if j not in n_dict:
    result.append(0)
  else:
    result.append(n_dict[j])
print(result)


