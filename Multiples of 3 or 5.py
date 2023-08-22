def sum_of_multiples(limit):
    total_sum = 0
    for num in range(limit):
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num
    return total_sum

limit = 10000000
result = sum_of_multiples(limit)
print("Сумма всех чисел, кратных 3 или 5, ниже", limit, ":", result)