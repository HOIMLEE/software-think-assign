import sys
input = sys.stdin.readline

K, L = map(int, input().split())

waiting_list = {}
for i in range(L):
    student_num = input().rstrip()
    waiting_list[student_num] = i

waiting_list = sorted(waiting_list.items(), key=(lambda x: x[1]))


cnt = 0
for student in waiting_list:
    print(student[0])
    cnt += 1
    if (cnt >= K):
        break
