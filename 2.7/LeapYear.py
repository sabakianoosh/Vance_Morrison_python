def is_leap_year(year):
    if year%400==0:
        return True
    elif year%4==0 and year%100!=0:
        return True
    else:
        return False
        

def days_in_month(year,month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        if is_leap_year(year):
            return 29
        return 28
    else:   
        return 30





