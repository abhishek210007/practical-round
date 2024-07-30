def palindrome(s:str):
    Str=''
    count=0
    L=len(s)
    for i in range(L):
        
        if s[i]!= s[L-1-i]:
            count+=1
            
            #Str=s[L-1-i]
            #Str[]=s[L-1-i]
            #Str= s[L-i-1] + s
    a= len(Str)-len(s)
    return count

S = "abc"
x = palindrome(S)
print(x)         