
# creating class
"""class Student:
    name = " karan "
    rollno="G05"

# creating object( instance  of class )

s1 = Student()
print(s1.name )
print(s1.rollno)
s2= Student()
print(s2.name )

class Car:
    color= "blue"
    brand = "mercedes "

car1 = Car()
print(car1.color ) 
print(car1.brand)
 
 #__init__ method

 #creating class
class Student:
    college_name= "ABC College" #class atr
    #deafult constructors
    def __init__(self):
        pass
    #parameterized constructor
    def __init__( self,fullname, marks):
        self.name=fullname
        self.marks= marks 
        print("adding new student in database")
        
        
#creating object 
s1=Student("karan",  100)
print(s1.name, s1.marks)

s2=Student("sahil", 98)
print(s2.name, s2.marks)  
  
print(s1.college_name)

print(s2.college_name)
 
     #methods

#creating class 

class Student :
    def __init__(self,fullname, marks):
        self.marks=marks
        self.name=fullname
        def welcome (self):
            print("welcome student!," , self.name)
            def get_marks(self):
                return self.marks
#creating class
    def hello(self):
       print("hello", self.name)
        
#creating object
s1=Student("karan")
s1.hello()
def welcome(self, name):
    print("welcome student ," , self.name)
def get_marks(self, marks ):
   return self.marks

s1=Student(" kamala", 89)
s1.welcome()
print(s1.get_marks())
"""
"""
class Student:
    def __init__ (self , fullname, marks ):
        self.name = fullname
        self.marks= marks
    def get_avg(self): 
       sum=0
       for val in  self.marks:
          sum += val
       print("hi", self.name , " your average score is :" , sum/3)
s1= Student("tony shark", [89 , 98, 91]) 
s1.get_avg()

s1.name= "ironman"
s1.get_avg()"""
#class Student:
#   @staticmethod   #decorator 
#  def college():
#       print('ABC college')
#create account class with 2 attributes - balance and account number,
#  create methods for debit ,
#  credit and printing the balance 
class Account:
    def __init__(self, bal, acc):
        self.balance= bal
        self.account_number=acc


        #debit method
        def debit(self, amount):
            self.balace-= amount
            print("Rs." , amount , "was debited from your account ")
            print("total balance =" , self.get_balance())
        #credit method 
        def credit(self, amount):
            self.balace += amount
            print("Rs." , amount , "was credited  from your account ")
            print("total balance =" , self.get_balance())

        def get_balance(self):
            return self.balance



acc1= Account(1000, 123456)
acc1.credit(21344)
acc1.debit(42313)
