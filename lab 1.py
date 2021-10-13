#lab 1-functions

#Exercise 2.2.

#1. The volume of a sphere with radius r is 4/3(pi)r^3. What is the volume of a sphere with radius 5?


def volume_sphere(radius, pi):
    formula = 4/3*(pi)*radius **3
    print("The volume of a sphere with radius is:", formula)

volume_sphere(5,3.1415926535897932)

# or i can do this if i want the user to enter the radius 5

def Inputradius():
    radius = input("Enter your radius: ") # Enter number 5
    return int(radius)  #because its a str so needs to convert it to int

def Formula(number):
    formula = (4/3*(3.1415926535897932)*number**3)
    return (formula)

def Output(caption,value):
    print(caption,value)

def Sphere():
    radius = Inputradius()
    formula = Formula(radius)
    Output("The volume of a sphere with radius is:", formula)
    
Sphere()


# or I can do this if i want the user to enter the radius

def Inputradius():
    radius = input("Enter your radius: ") # Enter number 5
    return int(radius)  #because its a str so needs to convert it to int

def Formula(number):
    formula = (4/3*(3.1415926535897932)*number**3)
    print("The volume of a sphere with radius is:", formula)

def Sphere():
    radius = Inputradius()
    formula = Formula(radius)
    
Sphere()


'''2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies?'''



#Parameters:  bookprice, discount, initialshippingcost, additionalcopycost, numberofcopies


def wholeSaleCost(bookprice, discount, initialshippingcost, additionalcopycost, numberofcopies):
    DiscountBookPrice = bookprice * discount
    firstcopyCost = DiscountBookPrice + initialshippingcost
    numberOfAdditionalCopy = numberofcopies-1
    totalCost = float( firstcopyCost + (DiscountBookPrice + additionalcopycost) * numberOfAdditionalCopy)
    print ("The total Whole Sale Cost for 60 copies is: ",totalCost)

wholeSaleCost(24.95, 0.6, 3, 0.75,60)


#or i can do this

def WholeSaleCost(bookPrice):
    Discount = bookPrice *0.6
    initialshippingcost = Discount+3
    additionalcopycost = (Discount +0.75) * 59 
    sum = initialshippingcost + additionalcopycost
    print( "The total Whole Sale Cost for 60 copies is: " ,sum)

WholeSaleCost(24.95)

-
'''3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?'''



def breakfasttime(pace,distance):
    
    Numpace = pace/60.0
    Distance = distance
    runtime = Distance * Numpace
    return runtime


def calculator():
    initialtime = 6 +52/60.0
    firstpace = (breakfasttime((8+15/60.0),1))
    secondpace = (breakfasttime((7+12/60.0),3))
    thirdpace = (breakfasttime((8+15/60.0),1))
    total_hr = (initialtime + firstpace +secondpace + thirdpace)
    total_min = (total_hr - int(total_hr))*60           
    print ('I will get home for breakfast at',int(total_hr), ":", int(total_min))

calculator()







