#del keyword 
# The del keyword is used to delete a reference to an object.
# It can be used to delete an entire object or just a single attribute of an object.+ 

class Student :
    def __init__(self , name ):
        self.name= name 
s1= Student ("shraddha ")
print(s1.name)
# Deleting an object    
del s1.name
 # this will give an error because s1.name is deleted
   
#explaining the  concept of private entity in oop
class Account:
    def  __init__(self, acc_no, acc_pass):
        self.acc_no= acc_no
        self.acc_pass= acc_pass
acc1= Account("123456789", "password")
print(acc1.acc_no)
print(acc1.acc_pass)
# The above code will print the account number and password
# However, it is not a good practice to expose sensitive information like passwords directly.
# To make the password private, we can use a single underscore before the attribute name.



class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no= acc_no
        self.__acc_pass = acc_pass #private attribute 
    def reset_pass(self):
        print(self.__acc_pass)



acc1= Account("123456789", "password")
print(acc1.acc_no)
# The above code will print the account number
print(acc1.reset_pass()) # This will give an error because __acc_pass is private
# To access the private attribute, we can use a getter method.


        


