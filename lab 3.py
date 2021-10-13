#lab 3- Classes and Lists

'''
Design 2 classes:

1.  A Student class.  The class contains two data strings; the first name and the last name

2.  A Course class.  The class contains a List of students.

Implementation:

A.  Read the Students from the Students.txt file.  Each line in the file contains he
    First, Last name of a student.  

B.  Read a line from the file.  Use the string rstrip function to remove the
    new-line character from the end of the line.  Use the string split function to split
    the First name from the Last name based on a comma.
    See the FileReader function in the Loops.py file in the Loops Module on Canvas for
    an example of reading from a file.  See the SplitString function in the Strings.py
    file for an example of using the Python split function.

C.  Store each student in the Course list.  The Course list is a data member of the Course class.  

D.  After reading the students, Sort the students by Last name.  The List object has
    a built-in sort function, so instead of using an external sort functions,
    as shown in Element.py, use the built-in sort function.
    Note that the Element.py file has a BubbleSort and LinearSearch.
    Don't copy these functions. Use the searching and sorting capabilities supplied by Python.
    See the ElementS.py file for an example of using these built-in functions.

E.  Output the sorted students.

'''


class Student:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

class Course:
    def __init__(self,courseList):
        self.courseList = courseList
    
    def CourseList(self):
        return self.courseList


OpenFile= open("Students.txt","r")

course = Course([])

for StudentName in OpenFile.readlines():
    
    StudentName= StudentName.rstrip().split(',')
    student = Student(StudentName[0],StudentName[1])
    course.CourseList().append(student)

OpenFile.close() 


course.CourseList().sort(key = lambda x :  x.getLastName(),reverse = False)
print("Below is the list of student names that are sorted by their last name:\n")
print ("FirstName\t", "LastName")
print ("-------------------------------------------------------")
for i in course.CourseList():
    print(i.firstName,",",i.lastName)

