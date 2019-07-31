import random
def test_1(A):
    current_value = 0
    counter = 0
    if (A[current_value] == -1):
        print (1)
        return 1

    while (current_value != -1):
        counter += 1
        current_value = A[current_value]

    print (counter)
    return counter



A = [1,4,-1,3,2]
test_1(A)

A_test1 = []
for x in range(1, 199998):
    A_test1.append(x)
A_test1.append(-1)

test_1(A_test1)

A_test2 = [-1]
test_1(A_test2)
