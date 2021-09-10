

def swap_case(s):
    strr=""
    for i in range(len(s)):
        if s[i].islower():
           strr=strr+ s[i].upper()
        elif s[i].isupper():
           strr=strr+  s[i].lower() 
        else:
            strr=strr+  s[i]
    return strr

s=swap_case(input())
print(s)

        
        
         

