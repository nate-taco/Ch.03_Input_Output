# Sign your name:________Nathan Topolinski________
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name = input("Please enter your name: ")
print("WELCOME", name, ", to the area,circumference,and square root calculator")
# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base = float(input("Please input the base of your triangle: "))
height = float(input("Please input the height of your triangle: "))
area = base*height
print("the area of your triangle is", area, "cubic units")
# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius = float(input("Please input the radius of your circle: "))
circumference = 2*3.14*radius
print("the circumference of your circle is", circumference, "cubic units")
# 4. Ask a user for an integer and then print the square root.
integer = float(input("Please input an integer: "))
square_root = integer**.5
print("the square root of your number is", square_root,)
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. 
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
Acceleration = float(input(print("please input an acceleration:  ")))
mass = float(input(print("Please input a mass:  ")))
Force = mass*Acceleration
print("may the mass * acceleration be with you", Force,)
print("get it?")