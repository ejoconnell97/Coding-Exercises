import numpy as np
def daily_coding_2_v1(A):
    B = []
    for x in range(0, len(A)):
        num = np.prod(A) // A[x]
        B.append(num)
    print (A)
    print (B)

def daily_coding_2_v2_nodiv(A):
    B = []
    

    # If I can't divide, then have a counter to keep track of current position
    # Multiply values except the current one
    for x in range(0, len(A)):
        num = 1
        for y in range(0, len(A)):
            if (y != x):
                num *= A[y]
        B.append(num)
    print (A)
    print (B)


input_array = [1,2,3,4,5]
daily_coding_2_v1(input_array)
daily_coding_2_v2_nodiv(input_array)
