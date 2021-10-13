#lab 2- Elementary Classes


#Exercise 2.2.

#1. The volume of a sphere with radius r is 4/3(pi)r^3. What is the volume of a sphere with radius 5?

import math
class VolumeofSphere:

    def __init__(self, r):
        self.radius = r
        self.volume = r * r * r *(4/3)* math.pi

    def calculate_r(self):
        return self.volume

radius = VolumeofSphere(5)
print ("The volume of the sphere is",radius.calculate_r())



'''2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies?'''

class Book:
    def __init__(self,price,discount,initialshippingcost,additionalcopycost,numberofcopies):
        self.price=float(price)
        self.discount=float(discount)
        self.initialshippingcost=float(initialshippingcost)
        self.additionalcopycost=float(additionalcopycost)
        self.numberofcopies=float(numberofcopies)
        self.total= (price*numberofcopies*discount)+initialshippingcost+(numberofcopies-1)*additionalcopycost

       
    def get_totalprice(self):
        return self.total

r=Book(24.95,0.6,3.0,0.75,60.0)
print("the wholesale price is",r.get_totalprice())



'''3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?'''



class BreakkfastTime:
    def __init__(self,min,second,distance):
        
        self.min=min
        self.second=second
        self.distance=distance
        self.total = ((min+second/60.0)/60.0)*distance
        
    def cal(self):
        return self.total
        
a= BreakkfastTime(8,15,1)
b= BreakkfastTime(7,12,3)
c= BreakkfastTime(8,15,1)
initialtime=6+52/60.0
runtime=(a.cal())+(b.cal())+(c.cal())
totalhour = initialtime+runtime
totalmin = (totalhour-int(totalhour))*60

print ('I will get home for breakfast at',int(totalhour),":", int(totalmin))
