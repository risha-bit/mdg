
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

#Write a Python program that lists all files of a given extension in a specified directory.
import os #imports the operating system module
def list_files_with_extension(directory, extension): 
    #directory = the folder to search in (like your bedroom)
    #extension = the type of file to look for (like .txt, .jpg, .mp3)
    if not extension.startwith("."):
        extension = extension +"."
        # Now we have the proper format: ".txt" instead of just "txt"
    try:
        files =os.listdir(directory)
        matching_files= [files for file in file if file if file.endswith(extension)]
        # This means "try to do this, but if something goes wrong, don't crash!"
        if matching_files:
           print(f"file with extension , {extension} in {directory}:")
        for file in matching_files:
            print(file)
        else:
           print(f"no files extension with{ extension} found in {directory}")
    except FileNotFoundError:
           print(f" the directory{ directory} is NOT found")
    except Exception as e :
        print(f" as ERROR occured : {e}")
directory =input("enter the directory path :")
extension =input(" enter the extension files (e.g: .txt):")
list_files_with_extension(directory, extension)


#Display the first and last colors from a given list
color_list = ['red','blue','black','yellow']
print('%s %s' % (color_list[0],color_list[-1]))

#Write a Python program that prints the second and second-last colors from a given list.
number_list =[12,23,33,45,56,67,78,89]
print("%s %s" %(color_list[1] , color_list[-2]))

#Write a Python script that takes a list of colors and prints them in reverse order.
colors= ['yellow','blue', 'black', 'blue']
colors.reverse()
print(colors)

#Write a Python program that takes a list of colors and finds the longest color name.
colors =['yellow', 'blue', 'black','green', 'turquoise', 'violet']
longest_color = max(colors, key= len )
print(" the longest color name is:", longest_color)

colors = input(" enter the color name seperated by commas :").split(',')
colors= [color.strip() for color in colors]
longest_color =max(colors, key =len)
print(" the longest name in the color is :", longest_color)

#Write a script to check if a specific color exists in the given list.
colors = ['yellow', 'blue','black', 'margerite', 'green','red', 'indigo']
color_to_check =input(" enter the colors to check :").strip(',').lower()
color_lower= [color.lower()  for color in colors ]
if color_to_check in color_lower:
    print(f" yes !! , { color_to_check } is in the list ")
else:
    print(f" no !!!, {color_to_check} is NOT in the list")

#Python: Display a sample examination schedule
#Write a Python program to display the examination schedule. 
# (extract the date from exam_st_date).
exam_date = (11,12,2025)
print(" the examination will start from : %i/%i/%i" % exam_date)

#Write a Python program that takes a tuple of exam dates
# and prints them in "Month Day, Year" format.
from datetime import datetime
exam_dates =(" 2025-01-10", " 2025-12-02","2025-09-11")
print(" Formatted Exam Dates:")
for date_str in exam_dates:
    try:
        clean_date = date_str.strip()
    #convert string into datetime object
        date_obj = datetime.strptime(clean_date  , "%Y-%m-%d")#datetime.strptime() → Parses a string into a datetime object.
    #formats the date as "Month Day, Year"
        formatted_date = date_obj.strftime(" %B %d , %Y") # %B = Full month name, %d = day, %Y = 4-digit year.
        print(formatted_date) #strftime() → Formats the date object into a readable format.
    except Exception as e :
        print(f' Error processing as a date { date_str} : {e}')

#Write a Python script that calculates how many days remain until an exam.
from datetime import datetime 
exam_date_str = input("enter the exam date('YYYY-MM-DD') : ")
#converts string to datetime object
exam_date = datetime.strptime(exam_date_str.strip() , "%Y-%m-%d")
#get today's date 
today = datetime.today()
#calculate the difference 
days_remain = (exam_date -today).days
if days_remain >0:
    print(f" your exam date is {days_remain} days")
elif days_remain==0:
    print(f" your exam is today ! GOOD LUCK")
else:
    print(f" your exam {-days_remain} days ago")

#Write a Python program that extracts and prints only the year from an exam schedule tuple
from datetime import datetime 
exam_schedule = (" Maths ", "2025-09-02")
#extract date string from the tuple
exam_date = exam_schedule[1]
#convert the string to date object 
date_obj = datetime.strptime(exam_date, "%Y-%m-%d")
print(" exam year:",  date_obj.year) 

#Write a script that takes multiple exam dates as input and prints the earliest one.
from datetime import datetime 
n= int(input(" enter the number of exam dates :"))

dates = [ ]
for i in range (n):
    date_input =input(f" enter the exam date {i+1} (DD-MM-YYYY)")
    try:
        date_obj = datetime.strptime(date_input, "%d-%m-%Y")
        dates.append(date_obj)
    except ValueError:
        print("invaild date format !! Please use DD-MM-YYYY")
#find the earliest date
earliest_date = min(dates)
print(" earliest exam date :", earliest_date.strftime("%d-%m-%Y"))

from datetime import datetime 
n= int(input(" enter the number of exam dates :"))
dates=[]
for i in range (n):
    date_input =input(f"enter the exam date {i+1} (DD-MM-YYYY): ")
    try:
        date_obj = datetime.strptime(date_input, "%d-%m-%Y")
        dates.append(date_input)
    except:
        print(" Invalid exam date format  (DD-MM-YYYY)")
        exit()

earliest_dates = min(date_obj)
print(f"Earliest exam date:", earliest_dates.strftime("%d-%m-%Y"))


#Python: Input an integer (n) and computes the value of n+nn+nnn
a = int(input(" Enter an integer:"))
n1 =int("%s" % a )
n2 =int("%s%s " %(a,a))
n3 =int("%s%s%s " % (a,a,a))
print(n1+n2+n3)

#Write a Python program to compute the value of n+nn+nnn+nnnn for a given integer n.
a = int(input("Enter an integer :"))
n1 =int("%s" % a)
n2 =int("%s%s" %(a,a))
n3= int("%s%s%s" % (a,a,a))
n4 =int("%s%s%s%s" % (a,a,a,a))
print(n1+n2+n3+n4)

#Write a Python program to compute the value of n+nn+nnn+nnnn for a given integer n.
n=int(input('Enter an integer :'))
term1 = int(n)
term2 = int(n*2)
term3 = int(n * 3)
term4 = int(n *  4 )
result = term1 + term2 + term3 + term4
print(f" {n} +{n*2} +{n*3} +{n*4} = {result}")

#Write a script that calculates n+nn+nnn but allows the user to input any number of repetitions.
n = input(" enter the digits (0-9): ")
r = int(input(" enter the number of repetitions :"))
total=0
pattern = ""
#build and add each term like n,nn,nnn
for i in range (1, r+1):
    pattern += n #creates n ,nn,nnn, pattern
    total += int(pattern) #converts int and add total 
print(f" sum of n +nn +... {r} times: % {total}")

#Write a Python program that prints each step of the calculation of n+nn+nnn
n = input(" enter single-digit number :")
#generate nn and nnn
nn =n*2
nnn = n*3
#convert integer for calculation
n_int = int(n)
nn_int = int(nn)
nnn_int = int(nnn)
#print each step 
print(f" 1st step :{n_int}")
print(f" 2nd step : {nn_int}")
print(f" 3rd step : {nnn_int}")
print(f" final calculation : {n_int} + {nn_int} + {nnn_int} =  {n_int + nn_int + nnn_int}  ") 

#Write a script that performs the same calculation
#but allows input with decimals instead of integers.
n = float (input(" enter the integer : " ))
#build nn and nnn string repetition
nn  = n* 2
nnn = n*3
#convert to floats
n_float  = float(n)
nn_float = float(nn)
nnn_float= float(nnn)
#print each step
print(f" step 1 : { n_float }")
print(f" step 2 : { nn_float }")
print(f" step 3 : { nnn_float }")
print(f" {n_float} + { nn_float} +{nnn_float } ={ n_float+ nn_float + nnn_float }")

#11. Function Documentation Printer

#Write a Python program to print the documents (syntax, description etc.)
#of Python built-in function(s).
function_name = input(" enter the name  of the built-in function : ")
try:
    print(f" documentation for {function_name} : ")
    help(eval(function_name ))
except Exception as e :
    print("error as e:", e)

function_name = input(" enter the name of the built-in function name :")
try:
    func =eval(function_name)
    print(f"the doc string for { function_name}")
    print(func.__doc__)
except Exception as e :
    print("error :" , e) 


#Write a Python program to print the documentation of any built-in function entered by the user.
func_name  = input(" enter the name of  built- in function :")
try:
    func = eval(func_name)
    print(" Documentation using __doc__ :")
    print(func.__doc__)
    print(" detailed explaination of the built-in function :")
    help(func)
except NameError: 
    print(" the function doesn't exist or you typed the wrong function name ")
except Exception as e:
    print(" an error occured :", e)

#Monthly Calendar Display
#Write a Python program that prints the  calendar for a given month and year.
import calendar
y =int(input(" enter the year : "))
m=int(input(" enter the month :"))
print(calendar.month(y,m))

#modified version 

import calendar
y = int(input(" enter the year :"))
month_name = input(" enter the month name (e.g : januart, february, march )")
if month_name in calendar.month_name :
    m=list(calendar.month_name).index(month_name)
    calendar.month_name(y,m)
else:
    print(" invalid month name")

#Write a Python program to display a calendar for an entire year.
import calendar
year = int(input(" enter the year :"))
print(f" Calendar of the  Year {year}!!!!")
print(calendar.TextCalendar().formatyear(year, width = 2 , lines= 3))

#Write a script that takes a date and prints the weekday name.
import datetime 
year =int(input("enter the year : "))
month = int(input(" enter the month:"))
day = int(input(" enter the day: "))
try :
    date = datetime.date(year, month,day) #create a date object
    weekday =date.strftime("%A") #gives full weekday name like Monday
    print(f" the date { day } falls on { weekday}")
except  ValueError:
    print(" Invalid date !! please enter the right month, date and week")


#Write a Python program that prints the number of days in a given month.
import calendar
year = int(input(" enter the year :"))
month = int(input(" enter the month (1-12): "))
# check if the month is valid 
if 1<= month <=12:
    #get the number of days using calendar module 
    days_in_month = calendar.monthrange(year,month)[1] # (first_weekday , number_of_days) 
   #first_weekday=  the day of the week the month starts on (0 = Monday, 6 = Sunday).
   # number_of_days = how many days are in that month.
    print(f" the number of days in {calendar.month_name[month]} {year} is :{days_in_month}")
else:
    print(" invalid month ! please enter the value between 1 -12 ")



#Write a script that highlights the current day when printing a monthly calendar.
import calendar 
import datetime
today = datetime.date.today()
year = today.year
month = today.month 
current_day = today.day
cal = calendar.TextCalendar() #create a TextCalendar
# Generate the calendar as a multiline string
month_str= cal.formatmonth(year,month)
highlighted_calendar = ""
for line in month_str.splitlines():
    new_lines = ""
    for item in line.split():
        if item.isdigit() and int(item) == current_day:
            item = f" <{item}> "
        new_lines += item.rjust(4)
    highlighted_calendar += new_lines +"\n"
print(highlighted_calendar)

#Write a Python program to calculate the number of days between two dates.
from datetime import date 
f_date = date(2025,1,13)
l_date = date(2024,1,13)
delta =l_date - f_date 
print(delta.days)

#Write a Python program that calculates the 
#number of weeks between two given dates.
from datetime import datetime
date1 = datetime.strptim("13-01-2025" , "%Y-%m-%d")
date2 = datetime.strptime("28-07-2025", "%Y-%m-%d")
days_diff = abs((date2 - date1).days)
  #convert days to weeks 
weeks = days_diff // 7
remaining_days = days_diff % 7 
print(f" weeks between the dates : { weeks} ful week (s) and {remaining_days} day(s)")

#Write a script that takes two dates as input and prints the difference in hours.
from datetime import datetime
def calculate_hours_difference (date_str1, date_str2):
    #define the expected date format
    date_format = "%Y-%m-%d  %H:%M:%S"
    try:
        #convert strings to datetime objects
        date1 = datetime.strptime(date_str1 , date_format)
        date2 = datetime.strptime(date_str2, date_format)
    except ValueError:
        print("Error : Dates must be in 'YYYY-MM-DD HH:MM:SS' format")
        return
    
    #calculate the  difference 
    time_difference = abs (date2 -date1)

    #convert difference to hours 
    hours_difference  = time_difference.total_seconds()/3600
    print(f" Time difference : { hours_difference: .2f} hours ")

if __name__ == "__main__" :
    #prompts for user input
    date_input1 = input(" enter the first date (YYYY-MM-DD HH:MM:SS) :")
    date_input2 = input(" enter the second date (YYYY-MM-DD HH:MM:SS) :")
    calculate_hours_difference(date_input1, date_input2)

#Write a Python program that calculates the number of days until the next New Year's Day.

from datetime import datetime, date 

def days_until_next_year():
    today = date.today() #gets today’s date from the system (like 2025-07-28)
    #create a date object for january 1st of the next year
    next_year = date(today.year +1 , 1,1 )
    #calculate the difference in days 
    delta = next_year - today
    print(f" days until the next new year : {delta} days ")

days_until_next_year() #run the function 


#Write a script that checks if a given date falls on a weekend.
from datetime import datetime
# ask the user to input the date 
date_str = input(" enter the date (YYYY-MM-DD) :")
#convert the string to datetime object
date_obj = datetime.strptime(date_str , "%Y-%m-%d")
#get the weekday number (0=monday , 6=saturday)
week = date_obj.weekday()
#check if its saturday or sunday
if week == 5:
    print(" the date falls on SATURDAY")
elif week==6:
    print(" the date falls on SUNDAY ")
else:
    print(" the date is weekday")

#Write a Python program to get the volume of a sphere with radius six
pi =3.1416
r=6.0
v=(4.0/3.0) * pi* r**3 #voume of the sphere (4/3)*pi*r**3
print(f" the volume of the sphere :{ v}")


#Write a Python program to calculate the surface area of a sphere given its radius.
#surface area of the sphere is 4*pi*r**2
import math 
r = float(input("Enter the Radius of the Sphere:"))
surface_area = 4*math.pi* r**2
print(f"surface are of the sphere is : {surface_area:.2f} square units ")

#Write a script that computes the volume of a cylinder given its radius and height.
import math 
def calculate_cylinder_volume(radius , height):
    volume = math.pi* radius ** 2 * height 
    return volume 
#example usuage 
if __name__ == "__main__" :
    radius = float(input(" Enter the radius of the cylinder :"))
    height = float(input("Enter the height of the cylinder :"))
#calculate the volume
    volume = calculate_cylinder_volume(radius , height )
    print(f" The Volume of the cylinder is :{volume:.2f} cubic units ")

#Write a Python program to find the volume of a cone given its radius and height
import math 
def cone_volume(radius , height ):
    volume = (1.0/3.0)*math.pi*radius**2*height
    return volume 
if __name__=="__main__":
    #take the input value of radius and height
    radius = float (input(" enter the value of radius of the cone : "))
    height = float(input("Enter the values of the height of the cone : "))
    volume= cone_volume(radius, height)
    print(f" the volume of the cone is: {volume:.2f} cubic units " )

