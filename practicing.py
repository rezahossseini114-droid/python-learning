#Creating Simple Variables
city= "Tehran"
name= "Reza"
age= 35
print(city)
print(age)
print(name)

#Addition and Multiplication of Two Numbers
a=3
b=5
print(a)
print(b)

#Celsius to Fahrenheit Conversion
celsius= 25
fahrenheit= ((9/5) * celsius)+ 32
print(fahrenheit)

#Creating a Sentence Using Variables (String Formatting)
fname= "Reza"
sname= "Hoseini"
year= 2025
sentence= f"Hi, I am {fname} {sname} and started programming in {year}."
print(sentence)

#Calculating the Length of a Text
text= "Hi, I am Reza Hoseini and started programming in 2025."
print(len(text))

#Finding the Remainder of a Division (Modulo)
x= 27
y= 19.4
print(x/y)
print(x%y)

#Updating a Variable’s Value Over Time
score = 0
score += 5
score += 10
score += 7

print(score)


#Integer Input
first_number= int(input("enter the first number: "))
second_number= int(input("enter the second number: "))
print (first_number + second_number)
#Float Input
first_number= float(input("enter the first number: "))
second_number= float(input("enter the second number: "))
print (first_number  + second_number)

#Basic Arithmetic Operations
first_number= float(input("enter the first number: "))
second_number= float(input("enter the second number: "))
sum = first_number + second_number
sub = first_number - second_number
mul = first_number * second_number
div = first_number / second_number
pow = first_number ** second_number
print (sum)
print (sub)
print (mul)
print (div)
print (pow)


#Input Validation
def get_float(prompt):
  check= True
  while check:
      try:
          a= float(input("enter the first number: "))
          check=False
      except ValueError:
          print("Invalid input. Please enter a valid float number.")
  return a
  
first = get_float("Enter the first number: ")
second = get_float("Enter the second number: ")

addition = first + second
subtraction = first - second
multiplication = first * second
division = first / second
power = first ** second

print("Sum:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Power:", power)


