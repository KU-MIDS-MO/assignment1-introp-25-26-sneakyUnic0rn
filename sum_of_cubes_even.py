def sum_of_cubes_even(n):
    ### Replace with your own code (begin) ###
        
    #return -1 if n < 0 or if n is not an integer
    if not isinstance(n, int) or n < 0:
        return -1
    
    #print warning
    if n > 2000:
        print ("WARNING: It gon take kinda long to calculate yall.. Your number is a bigus chungus!")
        
    sum = 0                             #declare 'sum' to use later
    for i in range (0, n+1, 2):         #start from 0 up until n while only counting even numbers
        sum += i ** 3                   #add all the cubed results
    return float(sum)                   #return as float
        
    ### Replace with your own code (end)   ###
