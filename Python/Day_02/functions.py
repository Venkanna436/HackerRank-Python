def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0 and year % 100 != 0 and  year % 4 == 0:   
        return True 
    return leap

year = int(input())




def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0: 
        leap = False
    elif year % 4 == 0:
        leap =  True        
    return leap

year = int(input())