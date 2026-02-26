import random

for _ in range(10):
    print(random.randrange(25, 36))


#Martin Sanchez
#Febuary 25 2026
#Problem 1 – randomrange.py
#Program Uses a for statement and random.randrange to print 10 random integers between 25 and 35

import random

odd_number = random.randrange(1, 101, 2)
print(odd_number)

#Martin Sanchez
#Febuary 25 2026
#Problem 2 – randomint.py
#Generate an odd number between 0 and 100

import random

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

selected_day = random.choice(days)
print(selected_day)

#Martin Sanchez
#Febuary 25 2026
#Problem 3 – randomday.py
#Program uses random.choice to select a day of the week from a list and print that day.

import math

# Simple approximations
approx1 = 22 / 7          # classic approximation
approx2 = 355 / 113       # accurate rational approximation

print("Approximation 22/7:", approx1)
print("Approximation 355/113:", approx2)
print("math.pi:", math.pi)

#Martin Sanchez
#Febuary 25 2026
#Problem 4 – pi.py
#Program computes the approximation and then prints the value as well as the value of math.pi from the math module.

import math

# User input
radians = float(input("Enter an angle in radians: "))

# Manual conversion
degrees_manual = radians * (180 / math.pi)

# Math.degrees
degrees_math = math.degrees(radians)

print("Manual conversion:", degrees_manual)
print("math.degrees conversion:", degrees_math)

#Martin Sanchez
#Febuary 25 2026
#Problem 5 – degrees.py
#Program computes the conversion given a user input value.
#Prints the value as well as the calculated value using the degrees function in the math module.

import math

# User input
n = int(input("Enter a non‑negative integer: "))

# Calculates factorial using a for loop
fact = 1
for i in range(1, n + 1):
    fact *= i

print("Factorial using loop:", fact)
print("Factorial using math.factorial:", math.factorial(n))

#Martin Sanchez
#Febuary 25 2026
#Problem 6 – factorial.py
#Program uses a for statement to calculate the factorial of a user input value.
#Prints the value as well as the calculated value using the factorial function in the math module.






