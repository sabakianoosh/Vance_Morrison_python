def average_of_squares0(n):
    sum = 0
    for i in range(n):
        sum = sum + i**2

    print(f"{sum/n}" + " is the average of squares from 0 to " + f"{n-1}")

average_of_squares0(5)

def average_of_squares1(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**2

    print (f"{sum/n}" + " is the average of squares from 1 to " + f"{n}")

average_of_squares1(4)


