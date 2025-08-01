# OBJECT ORIENTED PROGRAMMING  

from  car  import Car

car_1= Car(" chevy ", " corvette", 2021, "blue")
car_2= Car(" toyota ", " camry", 2020, "red")

Car.wheels= 2
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)


car_1.drive()
car_1.stop()