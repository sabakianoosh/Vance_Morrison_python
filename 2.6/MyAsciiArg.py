def print_cone(n): #n is odd
    print(n*" "+"^")
    for i in range(1,n+1):
        print((n-i)*" "+(i)*"/"+"|"+(i)*"\\")

print_cone(7)

def rocketship():
    for i in range(1,9):
        if i%2==1:
            print(print_cone(i))
rocketship()
