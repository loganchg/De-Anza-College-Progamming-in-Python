'''
Lab 4 - Dictionaries
 
 Write a UDT (class) to contain MorseCode data, as read from the MorseCode.csv file.  Read each line from the MorseCode.csv file and convert it to a MorseCode object.  After constructing the MorseCode object, insert it into a MorseCode Container class containing a  Dictionary to hold MorseCode objects.  
  Convert this sentence to MorseCode by looking up each character in the dictionary and printing the MorseCode:
 
"THE QUICK BROWN POODLE JUMPED OVER THE LAZY FOX 123 TIMES"

'''

import csv

class MorseCode:

   def __init__(self):
       self.dict = {}

   def readCode(self):
       with open('MorseCode.csv', 'r') as file:
           reader = csv.reader(file)
           for i in reader:
               self.dict.update({i[0]:i[1]})
               
   def convertMorseCode(self,d):

       code = ''    
       for i in range(0,len(d)):
           if(d[i] != ' '):
               code += self.dict[d[i]]              
           else:
               code += ''        
       return code

def main():
      mc = MorseCode()
      mc.readCode()
      convertedCode = mc.convertMorseCode("THE QUICK BROWN POODLE JUMPED OVER THE LAZY FOX 123 TIMES")
      print("Below is the Morse code for 'THE QUICK BROWN POODLE JUMPED OVER THE LAZY FOX 123 TIMES'")
      print("\n"+convertedCode)

main()

   


