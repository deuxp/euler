# number = 2520
# stop = 0
# on = True
# off = False

# while on:
#     number += 1
#     for multiple in range(1, 20):
#         if number % multiple == 0:
#             stop += 1
#             if stop == 20:
#                 print(number)
#                 on = off
n = 1
for i in range(1, 21):
    n *= i
    print(i, n)
