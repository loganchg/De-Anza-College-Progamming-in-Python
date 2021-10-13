#Lab 6 - Object Oriented Programming

'''
In the movie “The Martian” 2015, the “Martian” (Matt Damon) devises a clever scheme of adapting the Ascii table to a 360° circle.
The numbers 0 thru 9 and A thru F are placed on cards spaced at 23 degrees increments in a circle around the Sojourner Martian lander:

Specifications

Select objects from the Sojourner image to implement an Object Oriented Design.
Implement a translation algorithm to convert Degrees to ASCII characters.   Use Regular Expressions to parse the data file.
Use comprehensions, maps, iterators or generators and lambdas where ever possible.  These places will likely be some looping logic.
'''


import re
import csv
import collections


    

class convertion:           

    def convert_algorithm(self):
        self.firstnumber = [int(int(self.firstnumber[i]//22.5) for i in range(self.firstnaumber) # we can check whether the number is fallen into 0-9 or a-f
        self.secondnumber = [int(int(self.firstnumber[i]//22.5) for i in range(self.secondnumber)
        # we can check whether the number is fallen into 0-9 or a-f
                             
    def convertoHex(self):
        firstlist =[] 
        secondlist[]
        firstlist= self.firstnumber # store the firstnumber into the first list
        secondlist = self.secondnumber #store the second number into the second list
    
    def converttoascii(self):
        self.convertion = [byte.decode() for i in self.convert_algorithm # convert the number in firstlist and secondlist in to ascii


        if firstnumber <22.5:
            return 0
        elif firstnumber<45.0 & firstnumber>67.5:
    
        
        elif firstnumber<90.0 & firstnumber>67.5:
     
class converteddata:
    def __data__(self, x)
        self.x = x
    def result(self)
        print(result)

converted_dict - {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'}

class storeddata:
    def __storethedata__ (self):
        self.convertedlist = []
        
    def __str__(self):
        storeddata = ''
        for i in self.converttoascii:
            storeddata = storeddata + i
        
        

def readfile(x):
    combinedemptylist=([])
    with open (x) as file:
    csv_reader = csv.reader(file)
    firstnumber = list(i.split(',')[0] for i in csv_reader)
    secondnumber = list(i.split(',')[1] for i in csv_reader)
    
    
def main()
        readfile(("HexDegrees.csv"))
        
   
   
main()
