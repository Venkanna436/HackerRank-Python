s = input()
alphanumeric = alphabet = digit = lowercase = uppercase = False
    
for char in s:
        if char.isalnum():
            alphanumeric = True
            
        if char.isalpha():
            alphabet = True    
     
        if char.isdigit():
            digit = True
            
        if char.islower():
            lowercase = True   
            
        if char.isupper():
            uppercase = True   
                
print(f"{alphanumeric}\n{alphabet}\n{digit}\n{lowercase}\n{uppercase}")  
