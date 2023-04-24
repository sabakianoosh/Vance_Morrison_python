def compute_change(n): #n<100
    m=100-n
    
    Q=int((m/25))
    D=int((m-(Q*25))/10)
    N=int(((m-(Q*25)-(D*10))/5))
    P=m-((Q*25)+(D*10)+(N*5))
    
    print(f"{Q}=quarters")
    print (f"{D}=dime")
    print(f"{N}=nickel")
    print(f"{P}=pennies")
    

    

compute_change(8)