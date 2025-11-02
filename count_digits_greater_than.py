def count_digits_greater_than(n, t):
    ### Replace with your own code (begin) ###
    
    #return -1 if n is not an integer or if n < 0
    if not isinstance(n, int) or n < 0:
        return -1
    
    #return -1 if t is not an integer or if not 0 <= t <= 9
    if not isinstance(t, int) or not (0 <= t <= 9):
        return -1
    
    count = 0               #declare 'count' to use later
    for i in str(n):        #change n into string to be able to compare each number i
        if int(i) > t:      #see if i is greater than t
            count += 1      #increase count if it is
            
    return count
    ### Replace with your own code (end)   ###
