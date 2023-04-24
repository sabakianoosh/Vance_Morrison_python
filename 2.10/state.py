def start():
    sum=0
    a=0
    result=[]
    while a!=-1:
        a=float(input("number: "))
        if a!=-1:
            result.append(a)
        for r in result:
            print(r)
            sum+=a 
    avr=sum/len(result)
    print(f"{avr}"+"=average")
    min=result[0]
    for r in result:
        if r < min:
            min=r
    print(f"{min}" + "=min")
    max=result[0]
    for r in result:
        if r > max:
            max=r
    print(f"{max}"+ "=max")
start()

