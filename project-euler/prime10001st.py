counter = 2
number = 4
maximum = 6
common_prime = [2, 3, 5, 7, 11, 13, 17, 19, 23]

while counter != maximum:
    prime = 0
    number += 1
    for x in common_prime:
        if number % x == 0:
            prime += 1
    if prime == 0:
        counter += 1
print(number, counter)
