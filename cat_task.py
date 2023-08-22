# def solution(start, finish):  
    
#     jumps = 0
#     while(True):
#         if (start + 3) <= finish:
#             jumps+=1
#             start+=3
#         else:
#             if (start + 1) <= finish:
#                 jumps+=1
#                 start+=1
#             else:
#                 break

#     return jumps


# print(solution(1,5))




def two_are_positive(a, b, c):
    if ((a and b) > 0) or ((b and c) > 0) or ((a and c) > 0):
        if a or b or c == 0:
            return True
    else:
        return False
    