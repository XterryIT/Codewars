t1 = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]  # should return 5 (because it appears 3 times)
t2 = [1,1,2,-2,5,2,4,4,-1,-2,5] # should return -1 (because it appears 1 time)
t3 = [20,1,1,2,2,3,3,5,5,4,20,4,5] #  should return 5 (because it appears 3 times)



def find_it(seq):
    answer = 0
    odd_counts = {}
    counts = {}

    for num in seq:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for key, value in counts.items():
        if counts[key] % 2 != 0:
            answer = next(iter(counts))


    return answer

print(find_it(t1))