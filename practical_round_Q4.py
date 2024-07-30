def happyNum(n):
    sum=0
    l=[]
    for i in range(2,100):
         
            
        while i>0:
            dig=i%10
            sum+=dig**2
            n//=10

        if sum== 1 :
            l.append(i)
    print(l)     
        
        
    

print(happyNum(8))