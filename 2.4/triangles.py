def left_triangle(n):

    for i in range(n+1):
        print("*"*i)

left_triangle(20)

def print_left_triangle(n,ch):
    for i in range (n+1):
        
        print(i*ch)

print_left_triangle(20,'%')

def print_right_triangle(n):
    for i in range(n):
        print((n-i)*" " + i*"*")

print_right_triangle(20)
    

    