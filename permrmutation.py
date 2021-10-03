li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
su = 0
total_sum = 1
i = 0
for i in range(10):
    su += li[i]
    total_sum += i
    if total_sum < su:
        print("The missing no is", total_sum)
        break
