'''
month: even and < 7 april and june (30)
       even and >7 aug, oct and dec (31)
       odd and <=7  jan, march, may ,july (31)
       odd and >7  sep , nov (30)
'''

import random
import datetime
def leap(yr):
    if yr%4==0:
        if yr %100==0:
            if yr%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
data=[]
months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
for i in range(40):
    yy=random.randint(1999,2023)
    if(leap(yy)):
        months[2]=29
    else:
        months[2]=28
    mm=random.choice(list(months.keys()))
    dd=random.randint(1,(months[mm]))
    datee=datetime.date(yy,mm,dd)
    day_of_weak=datee.timetuple().tm_wday # returns the day of the week like mon ,tues ---- sun (1,2,3,4,5,6,7)
    day_of_year=datee.timetuple().tm_yday
    data.append(day_of_year)
sum=0
for i in range(1,366):
    sum+=data.count(i)
    print(i,"  ",data.count(i))

print("\n\n",sum)
