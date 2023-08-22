def move_zeros(lst):
    temp = 0
    non_zeros = []
    for num in lst:
        if num != 0:
            non_zeros.append(num)
    zeros = [0] * (len(lst) - len(non_zeros))

    return non_zeros + zeros

move_zeros([1, 0, 1, 2, 0, 1, 3])