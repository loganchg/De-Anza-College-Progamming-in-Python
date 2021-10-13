'''
Using these lists:

     ones = [ "I","II","III","IV","V","VI","VII","VIII","IX" ]
     tens = [ "X", "XX","XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ]
     hundreds = [ "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM","M" ]

Convert these list to named tuples and store them in a class.
Then write a member function(s) for the class to convert a 'int' to a 'roman numeral'.
in the range of 1 to 1000.
Use comprehensions, map, reduce or join where appropriate.

'''


class Roman:
    def __init__(self,num):
        self.ones = tuple([ "I","II","III","IV","V","VI","VII","VIII","IX" ])
        self.tens = tuple([ "X", "XX","XXX", "XL", "L", "LX", "LXX", "LXXX", "XC" ])
        self.hundreds = tuple([ "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM","M" ])
        self.num = num
        self.convertNum()

    def convertNum(self):
        self.roman = ""
        if(self.num%10!=0):
            self.roman += self.ones[self.num%10 - 1]
            
        if((self.num%100)//10!=0):
            self.roman += self.tens[(self.num%100)//10 - 1]

        if(self.num//100!=0):
            self.roman += self.hundreds[self.num//100 - 1]
           
        
    def __str__(self):
        return self.roman
    
def main():

        number = int(input("Please enter an integer between 1 and 1000 and we will convert the int to Roman: "))

        if number > 1000:
            print ("Please try again! ")
            
        else:
            R = Roman(number)
            print("The number is converted below")
            print("You entered:", number, f"and in roman it is {R}")
            
main()

