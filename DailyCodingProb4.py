'''
Given a list of integers, positive or negative, find the smallest missing
positive integer in constant space and linear time
'''



def daily_coding_prob_4(A):
    B = set(A)
    C = set()
    answer = 1

    #if list is empty, return 1
    if not A:
        print (answer)
        return answer
    
    #if none of the values in A above zero, return 1
    if (max(A) <= 0):
        print (answer)
        return answer


    #as long as some values are above zero, initialize C with full range of
    #positive integers between 1 and max value of A
    for x in range(1, max(A)):
        C.add(x)

    #This should give list of all positive integers not in B
    D = list(C - B)


    #If the array is not missing any positive integers, return max of A + 1
    if not D:
        answer = max(A) + 1
        print (answer)
        return answer

    #If a value is missing, i.e. D is not empty, return the minimum value in D
    else:
        answer = min(D)
        print (answer)
        return answer


A = []
daily_coding_prob_4(A)

A = [-1,-2,-3,-4,-5]
daily_coding_prob_4(A)

A = [1,2,3,4,-1,1]
daily_coding_prob_4(A)

A = [2,4,1,5]
daily_coding_prob_4(A)
