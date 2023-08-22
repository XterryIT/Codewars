



def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

print(digital_root(71516))