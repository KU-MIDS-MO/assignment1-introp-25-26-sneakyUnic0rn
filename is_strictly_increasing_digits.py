def is_strictly_increasing_digits(n):
    ### Replace with your own code (begin) ###
    
    #return -1 if n < 0 or if n is not an integer
    if not isinstance(n, int) or n < 0:
        return -1
    
    str_n = str(n)                      #change n into string to be able to use each number i in n
    for i in range(len(str_n) - 1):     #for number of digits
        if str_n[i] >= str_n[i + 1]:    #if the number is larger than or equal to next number
            return False
    
    return True
    ### Replace with your own code (end)   ###
