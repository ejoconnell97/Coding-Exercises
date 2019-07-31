def test_2(A):
    # write your code in Python 3.6
    '''
    Loop through S once, saving each value to a new_password
    When a numerical character is hit, or end of S, check the new_password
        to make sure it has at least one uppercase letter
        - Yes, return it
        - No, reset string to null and continue through S
    If new_password is empty, return -1
    '''
    current_password = ""
    new_password = ""
    has_upper = False
    password_length = 0
    
    
    #loop through all of S
    for x in A:
        
        #if the current character is not a number
        if (x.isalpha()):
            current_password += x
            
            #update the new password if needed
            new_password, has_upper = update_string(current_password, new_password, has_upper)
        else:
            #update new_password if S ends with a number
            new_password, has_upper = update_string(current_password, new_password, has_upper)
                
            #otherwise, reset the current_password because you've reached a number
            current_password = ""
    
    
    if not new_password:
        return -1
    print (new_password)
    password_length = len(new_password)
    
    return password_length


#make sure that the current_password has at least one uppercase character and is longer than new_password before updating it    
def update_string(current, new, has_upper):
    for x in current:
        if x.isupper():
            has_upper = True
    if (has_upper == True and (len(current) > len(new))):
        new = current
    has_upper = False
    return new, has_upper
A = "a00000000000000aA9AAA"
test_2(A)
