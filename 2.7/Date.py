import LeapYear as lp
w1=[31,28,31,30,31,30,31,31,30,31,30,31]
w2=[31,29,31,30,31,30,31,31,30,31,30,31]

def month(mn):
    if mn in {1,3,5,7,8,10,12}:
        return w1[0]
    elif mn in {4,6,9,11}:
        return w1[3]
    elif mn==2:
        return w1[1]
    



def days_before_date(year,monthNumber, day):
    m=0
    if not  lp.is_leap_year(year):
        days=0
        for i in range(0,monthNumber-1):
            days+=w1[i]
            m=days+(day-1)
        print(m)
        return m
      
    if lp.is_leap_year(year):
        days=0
        for i in range(0,monthNumber-1):
            days+=w2[i]
            m=days+(day-1)
        print(m)
        return m


def day_of_the_week(year,monthNumber,day):
    b=0
    b=days_before_date(year,monthNumber,day)%7
    if b==1:
        print("Thursday")
    elif b==2:
        print("Friday")
    elif b==3:
        print("Saturday")
    elif b==4:
        print("Sunday")
    elif b==5:
        print("Monday")
    elif b==6:
        print("Tuesday")
    elif b==0:
        print("Wednesday")
day_of_the_week(2014,3,18)
        
