import math
def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial


def eulers_constant(precision):
    i=1
    sum=1
    while  1/factorial(i) > precision :
        sum = sum + (1/factorial(i))
        i=i+1
    return sum

eulers_constant(0.0001)


def power(x,i):
    if i >= 0:
        return (x**i)


def exp(x,precision):
    i=1
    sum=1
    while (x**i)/factorial(i) > precision:
        sum+=(x**i)/factorial(i)
        i+=1
    return sum
exp(2,0.000001)





def exp2(x,precision):
    sum=1
    i=1
    mul=1
    while mul > precision:
        mul*=x/i
        sum+=mul
        i+=1
    return sum
exp2(1,0.000001)


def abs(n):
    if n < 0:
        return -n
    return n

def near(x, y, closeness):
    if abs(x) > abs (y):
        if abs(y)+closeness*abs(x)>=abs(x):
            return True
        return False
    if abs(x) < abs (y):
        if abs(x)+closeness*abs(y)>=abs(y):
            return True
        return False
near(999,1000,0.001)

assert near(exp(1,0.0001),exp2(1,0.0001),0.00001)==True


def sin(x,precision):
    r=x*(math.pi/180)
    sum=0
    i=1
    w=((r**(2*i-1))/factorial(2*i-1))*((-1)**(i+1))
    while w > precision:
        w=((r**(2*i-1))/factorial(2*i-1))*((-1)**(i+1))
        sum+=w
        i+=1
    return sum
sin(45,0.000001)

def square_root(x, precision):
    assert 0<=x
    lowerbound=0
    upperbound=x
    while upperbound-lowerbound > precision:
        mid=(lowerbound+upperbound)/2
        if mid**2==x:
            return mid
        elif mid**2>x:
            upperbound=mid
        elif mid**2 < x:
            lowerbound=mid
    return mid
square_root(5,0.1)


def root(x, n, precision):
    lowerbound=0
    upperbound=x
    while upperbound-lowerbound>precision:
        mid = (upperbound+lowerbound)/2
        if mid**n==x:
            return mid
        elif mid**n < x:
            lowerbound=mid
        elif mid**n > x:
            upperbound=mid
    return mid
root(5, 2, 0.1)

def ln(x, precision):
    lowerbound=0
    upperbound=x
    while upperbound-lowerbound > precision:
        mid=(upperbound+lowerbound)/2
        if exp(x,precision)**mid == x:
            return mid
        elif exp(x,precision)**mid > precision:
            upperbound=mid
        elif exp(x,precision)**mid < precision:
            lowerbound=mid
    return mid
ln(2,0.001)
