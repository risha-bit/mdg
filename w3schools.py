
#. Reverse Full Name
#Write a Python program that accepts the user's first and last name
#and prints them in reverse order with a space between them.
fname =input(" enter your name :")
lname=input(" enter last name :")
print(" Hello " + fname + " " + lname )


#Python: Generate a list and tuple with comma-separated numbers

#*Write a Python program that accepts a sequence of comma-separated numbers from the user
#and generates a list and a tuple of those numbers.

value =input(" enter the values in comma - seperated :")
list = value.split(',')
tuple= tuple(list)
print(" the list is :", list )
print(" the tuple is :", tuple)

#Write a Python program that converts a list of numbers into a tuple and vice versa.
def list_to_tuple(lst):
    return tuple(lst)
def tuple_to_list(tup):
    return list(tup)
num_list=[1,2,3,4,5,6,7,8,9]
print("Original list :", num_list)

#convert list to tuple
num_tuple =list_to_tuple(num_list)
print(" the list converted to tuple:", num_tuple)

#the tuple is converted back to tuple(viceversa)
converted_list= tuple_to_list(num_list)
print(" the tupl is then converted to list :", converted_list)

#Write a Python script to take a comma-separated string input and create a sorted list and tuple.
value = input(" enter the value in comma-seperated form:")
num_list =[int(item.strip()) for item in value.split(',')]
l1= sorted(num_list)
converted_tuple =tuple(l1)
print("sorted list:", l1)
print(" convereted tuple:", converted_tuple)

#Write a Python program that removes duplicate numbers from a list before converting it into a tuple.
num_list =[1,2,3,4,5,6,5,4,3]
unique_list =list(set(num_list))
sorted_list= sorted(unique_list)
converted_tuple= tuple(sorted_list)
print(" the sorted list is :", sorted_list)
print(" the converted tuple:", converted_tuple)

#Write a script that takes a list of numbers, squares each number, and stores the results in both a list and a tuple.
num =input(' enter the values in  comma- seperated :').split(',')
square_num = [int(x)**2 for x in num]
square_list = list(square_num)
square_tuple= tuple(square_list)
print("the squared list is :", square_list)
print(" the squared tuple:", square_tuple)

#Python: File extension
#File Extension Extractor
#Write a Python program that accepts a filename from the user and prints the extension of the file.
filename = input(" enter the filename with extension: ")
extension =filename.split('.')
print(" the file extension of the file is :" , repr(extension[-1]))

#Write a Python program to extract and print the file name without its extension.
import os
filename_extension = "example.txt"
file =os.path.splitext(filename_extension)[1]
print(" the file name of the filename extension:", file)
