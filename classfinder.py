#Exercise 5: Create a class MaxFinder that identifies the largest number in a list.
"""
class MaxFinder:
    def __init__(self, numbers):
        self.numbers= numbers
    def find_max(self):
        if not self.numbers:
            return " list is empty"
        return max(self.numbers)
    #example usuage 
finder = MaxFinder([3 ,5, 7, 9, 0, 10, 7])
print(" the largest number in a list is : ", finder.find_max())

#Exercise 6: Design a Rectangle class with default attributes for length and width set to 1. Include methods to set these attributes and calculate the area.
class Rectangle:
    def __init__(self, length = 1 , breadth = 1):
        self.length = length 
        self.breadth = breadth 
    def set_dimensions(self, length, breadth):
        self.length = length 
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    
#example usuage 
rect= Rectangle()
print("default area of the rectangle:", rect.area())
rect.set_dimensions(8,9)
print("area of the updated rectangle is :" , rect.area()) 

#Exercise 7: Person Class with __str__ Method: Create a Person class with first and last name attributes 
# and override the __str__ method to return the full name.
class Person:
    def __init__(self, first_name , last_name):
        self.first_name = first_name 
        self.last_name = last_name 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
#example usuage
person= Person("Joe", 'Smith')
print(person) 

#Exercise 8: Student Grade Calculator: Implement a Student class with attributes for name and a list of marks.
# Include a method to calculate the average and determine the grade.
class Student :
    def __init__ (self, name, marks):
        self.name = name 
        self.marks = marks 

    def average(self):
        return sum(self.marks)/len(self.marks )
    
    def grade(self):
        average = self.average()
        if average >= 90:
            return "A"
        if average >= 80:
            return "B" 
        if average >= 70:
            return "C" 
        if average >= 60:
            return "D"
        else:
            return "F"
        

#example usuage 
student = Student("Alice" , [ 90, 91, 98 ])
print(f"{ student.name } Grade :{student.grade()}") 

#Exercise 10: Last Digit in Words: 
#Write a class with a method that takes an integer and prints the last digit of that number in words.
class NumberInWords:
    def last_digit_in_words(self, number ):
        if not isinstance(number, int):
            raise ValueError (" input must be an integer")
        last_digit= abs(number)%10
        words= ["zero" ,  "One", "Two", "Three", "Four", "Five", "Six", "Seven ", "Eight", "Nine"]
        return words[ last_digit]
#example usuage 
niw= NumberInWords()
print(niw.last_digit_in_words(123))
print(niw.last_digit_in_words(-127))

#Exercise 11: Object Count Tracker: Design a class that tracks 
#how many objects have been created from it and has a method to display this count.

#Class Variable count: This is shared by all instances of the class 
# and keeps track of the total number of objects created.

#__init__ method: This is the constructor that gets called each time a new object is created. 
# It increments the count variable by 1.

#display_count class method: This method displays the current count of created objects. 
# It's a class method (denoted by the @classmethod decorator) because it operates on class-level data rather than instance data.
class ObjectCounter:
    count=0
    def __init__(self):
        ObjectCounter.count+=1
    @classmethod
    def display_count(cls):
        print(f" the number of objects created :",  {cls.count})
if __name__ == "__main__":
       obj1=ObjectCounter()
       obj2=ObjectCounter()
       obj3=ObjectCounter() 
ObjectCounter.display_count()
obj4=ObjectCounter()
obj5=ObjectCounter()
ObjectCounter.display_count()

#Exercise 12: Calculating Student Results: Develop a class to accept a student's name
#  and marks in three subjects, then calculate and display the total and average marks.

class StudentResults:
    def __init__ (self, name , marks):
        self.name = name 
        self.marks= marks 
    def total(self):
        return sum(self.marks)
    def average(self):
        return self.total() / len(self.marks) 
    def display(self):
        print(f" the name is :{self.name }")
        print(f" the total mark is:{ self.total()}")
        print(f" the average  marks is : {self.average()}")
# example usuage 
sr = StudentResults('John smith ' , [ 90, 98, 97 ])
sr.display()

#Exercise 13: Car Class: Create a Car class with attributes make, model, and year. Include a method to display the details of the car.
class Car :
    def __init__(self, make , model , year ):
        self.make = make 
        self.model = model 
        self.year = year 
    def display_details (self ):
        print(f" make :{ self.make} , model :{ self.model } , year :{self .year}")
#example usuage 
c= Car (" toyotta " , " corolla ", 2020)
c.display_details()

#Exercise 14: Inheritance - Animal Kingdom: Create a base class Animal with a method speak().
#  Derive two classes Dog and Cat from Animal and override the speak method to reflect their sounds.
#Key Rules ✨
#Same Name: Method must match Mommy’s name (e.g., both use speak()).

#Same Inputs: Same parameters (like self in Python).




class Animal :
    def speak ( self ):
        pass 
class Dog ( Animal ):
    def speak (self ):
        print(" wooff")
class Cat (Animal):
    def speak(self ):
        print("meow ")
 #example usuage 
dog = Dog()
cat= Cat ()
cat.speak()
dog.speak()
"""
#Exercise 15: Polymorphism with a Function: Create a function describe_pet that takes an object of Animal 
#and calls its speak method, demonstrating polymorphism.

#Polymorphism (Greek for "many forms") allows objects of different classes to be treated as objects of a common superclass
# while executing the correct method based on their actual type.
class Animal :
    def speak(self):
        raise NotImplementedError (" subclass must implement this method ")
class Dog (Animal ):
    def speak (animal):
        print("woof! woof! ")
class  Cat (Animal):
    def speak(Animal):
        print(" meow meow !!!")
class  Parrot (Animal ):
    def speak(Animal):
        print(" squiwk squiwk!!!!")
def describe_pet(animal):
        animal.speak()
dog = Dog()
cat= Cat()
parrot= Parrot()
describe_pet(dog)
describe_pet(cat)
describe_pet(parrot)
 




