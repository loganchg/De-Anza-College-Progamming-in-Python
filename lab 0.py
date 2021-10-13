#lab 0- statements


#Exercise 2.2.

#1. The volume of a sphere with radius r is 4/3(pi)r^3. What is the volume of a sphere with radius 5?


radius = 5
pi = 3.1415926535897932

print ("The volume of a sphere with radius ",radius, "is", 4/3*(pi)*radius **3)


'''2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies?'''

# I can do this or the follow scripts for this problem
book = 24.95
shippingCost = 3
print ("The price of a book after 40 % discount: " , book * 0.6)
print("As the first copy is $3 and 75 cents for each additonal copy, the total whole sale cost for 60 copies is:",
      book*60*0.6+shippingCost+59*0.75)

#or this for question 2
book = 24.95
newBook_price = book *0.6
print("The price of the book is", book, "and after the 40% discount is" , newBook_price)
print("The shipping costs for the first copy is $3 and 75 cents for each additional copy")
shippingCost = 3
add_copy = 0.75
print("The total whole sale cost for 60 copies is", newBook_price*60+shippingCost+59*add_copy)


'''3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?'''


leaveHome = 6 + 52/60.0
EasyPace = (8 + 15/60.0) / 60.0
Tempo = (7 + 12 / 60.0)/60.0
runtime= 2*EasyPace + Tempo*3

total_timeHr= leaveHome + runtime
total_timeMin =(total_timeHr-int(total_timeHr))*60

print ('I will get home for breakfast at', int(total_timeHr), ":", int(total_timeMin))









