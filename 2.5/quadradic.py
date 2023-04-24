def quadradic(A,B,C):
    #A*(x**2) + B*x + C = y
    x1= (-B+(B**2 - 4*A*C)*0.5)/2*A
    x2= (-B-(B**2 - 4*A*C)*0.5)/2*A
    print (x1,x2)

quadradic(1,4,3)