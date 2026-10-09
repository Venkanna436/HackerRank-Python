def solve(s):
     s = s.split(' ')
     for word in range(len(s)):
         if s[word]:
             s[word] = s[word][0].upper() + s[word][1:]
            
     s = " ".join(s)
     return s      

s = input()
result = solve(s)