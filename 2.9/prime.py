def is_divisible(a,b):
    if a%b==0:
        return True
    elif a%b!=0:
        return False


def is_prime(N):
    assert 0 <= N
    for i in range(2,N):
        if N%i==0:
           return False
    return True
for N in range(2,100):
    if is_prime(N):
        print(N)

