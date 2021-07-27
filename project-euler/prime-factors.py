number = 600851475143
stop = 1
prime_factors  = []

for n in range(2, int(number)):
    if number % n == 0:
        stop *= n
        prime_factors.append(n)

    if stop == number:
        break
print(prime_factors, stop)
