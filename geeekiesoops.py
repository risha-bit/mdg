#Exercise 1: Create a class Greeter with a method greet(name) that prints a greeting for the provided name.
class Greeter: 
    def greet(self, name ):
         print(f"hello {name} !")
# example usage
g= Greeter()
g.greet(" Minora ") 


#Exercise 1: Create a class farwell  with a method say_goodbye(name) that prints a Goodbye  for the provided name.
class Farewell:
    def say_goodbye(self, name):
        print(f" Goodbye {name}")
#example usuage 
f=Farewell()
f.say_goodbye("jo")

class Function:
    def ceremony (self , name , age ):
        print(f'congratulations {name} on your {age}th  Birthday ')
#example usuage 
f=Function()
f.ceremony ("Minora", 19)


class Bank:
    def account(self, name):
        print(f"{name}'s  account created sucessfully")

    def deposit(self , cash):
        print(f"{cash} cash deposited ")

    def withdraw(self, cash):
        print(f"{cash} cash withdrawn")

    def balance (self):
        print("your balance is 10000")

#example usuage 
b = Bank()
b.account(" Minora")
b.deposit(9000)
b.withdraw(2000)
b.balance()


def program1():
    print(" output from program 1")
def program2():
    print(" output from program 2")

"""
#Exercise 2: Develop a class Calculator with methods to add and subtract two numbers.
"""
class Calculator:
    def add (self , a , b ):
        print("the sum of the number is : " ,a +b) 
    def substract (self, a , b):
        print(" the differnce of the number is :" , a-b)
    def multiply(self, a, b ):
        print(" the product of the number is :",  a*b)
    def divide (self, a, b):
        if b ==0:
            print("division by zero is not acceptable")
        else:
            print( "the divison of the number is :" , a/b)
    def modulus(self, a, b):
        print(" the modulus of the number is ",  a%b)
    def power(self, a, b):
        print(" the power of the number is ", a**b ) 
    def floor_division (self , a , b):
        print("the floor divsion of the number is ", a//b) 
    def square_root(self, a):
        print(" the sqaure root of the number is :",  a**0.5)
    def cube_root(self, a ):
        print(" the cube root of the number is :", a**(1/3)) 
    def factorial(self, a ):
        if a==0 or a==1:
            print(1)
        else: 
            fact = 1         
            for i in range (1, a+1):
                fact *= i
        print(" the factorial of the number is :", fact) 
    def logarithm(self , a , base):
        import math
        print(" the logarithm of the number is ", math.log(a, base )) 
    def exponential(self , a ):
        import math
        print(" the exponential of the numbr is :",math.exp(a) ) 
#example usuage 
c= Calculator()
c.add(2, 9)
c.substract(9,1)
c.multiply(9,7)
c.divide(8,0)
c.modulus(2, 7)
c.power(2,3)
c.floor_division(11,3)
c.square_root(64)
c.cube_root(8)
c.factorial(7)
c.logarithm(100, 10)
c.exponential(0)
"""
#Exercise 3: Build a class Employee with multiple constructors that can initialize an employee object in different ways.
"""
class Employee:
    def __init__(self, name , id= None , department= None ):
        self.name = name
        self.id = id 
        self.department = department 
    def display_details (self):
        print(f" Name :{ self.name }")

        if self.id:
            print(f" ID :{self.id}")

        if self.department:
            print(f" Departement: {self.department}")
#example usuage 
emp1= Employee (" John smith")
emp1.display_details()

emp2=Employee(" Desmond", 109, "HR")
emp2.display_details()

emp3= Employee("Chris", 123, "executive")
emp3.display_details()


#Exercise 4: Design a class SeriesCalculator that calculates the sum of an arithmetic series.

class SeriesCalculator:
    def calculate_sum(self, n, a, d):
        #sum of n terms of an arithematic series 
        return n * ( 2* a  + ( n - 1 ) * d ) // 2
    #test the calculate_sum method  
sc= SeriesCalculator()
print(" the sum of the series :", sc.calculate_sum(15,1, 2 ))