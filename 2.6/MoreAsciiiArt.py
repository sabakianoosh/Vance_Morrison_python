def print_left_triangle(n):
    for i in range(n+1):
        if i%2 == 0:
            print (i*"*")

        else :
            print (i*"%")

print_left_triangle(10)
