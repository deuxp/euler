a = 1
b = 2
c = 0
total = 0
limit = 4 * (10 ** 6)

while True:
    c = a + b
    if c >= limit:
        break
    if c % 2 == 0:
        total += c
    a = b
    b = c
print(total + 2, c, limit)
