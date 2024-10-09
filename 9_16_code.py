"""
Name:Matthew Harris
Date:9/16/2024
Assignment:Unit 2 Lesson 1 Notes
"""


# Variables - store information

message = "Hello, user"
print(message)

# snake_case to name our variables
user_name = input("Enter your name: ")
user_id = int(input("Enter your id: "))

#variable type
#print(type(user_name))


#Strings
# can use ' or " to indicate string - be consistent

# f-strings are formatted strings that help with combining string
# Way 1 to combine string: use + (concatenation)
#Caution: all numbers have to have str() around them
message_one = "Welcome " + user_name + " with ID " + str(user_id)
print(message_one)

#way 2 - use F strings
message_two = f"Welcome {user_name} with ID {user_id}"
print(message_two)

# Possible errors
#apostrophes inside of single quotes
#\ instead
#literally that thing, no Pythonic meaning
famous_quotation = 'Quotations are hard to find in the middle of lessons - its annoying. Mr.Smith'


# raw strings
cat = r"""
("`-''-/").___..--''"`-._ 
 `6_ 6  )   `-.  (     ).`-.__.`) 
 (_Y_.)'  ._   )  `._ `. ``-..-' 
   _..`--'_..-_/  /--'_.'
  ((((.-''  ((((.'  (((.-' 
"""
print(cat)

#Lesson 2 notes (talk to mr smith)
my_int=5
my_float=6.38
print(F"{my_int} {my_float}")
another_float=8.0#make a float by adding point 0
float_two = float(8)# make a float by casting
print(F"{another_float} {float_two}")

#ger a decimal from a user
radius = float(input("Enter a radius: "))
print(f"You entered a radius of {radius}")

# operations on numbers
# P E MMod D AS
#modulus operator or remainder operator'
print(15%7)#print the remainder when 15 is divided by 7
print((2+3)*4) # 2+3 first, times first

# exponent is not ^, it is **
print(5**4)# thus is 5^4
print(5^4)# this is not

# weird math stuff
print(0.3-0.2) # roundoff error - watch out for it

#rounding
#method 1, use round()
num = 3.1415
print(round(num,2))
#method 2
print(f"{num:.2f}")

#your turn to code
# Ask a user for some amount of US dollars
#store this in a variable
#conver that money to currency of your choice
# store the conversation factor in a variable
# s tore the final amount in a variable
#print it like "___ USD is the same as ___ CAD"
# round too 2 decimal places

usd_num = float(input("Pick a random amount of USD: "))
conversion_factor = 1.34
pounds = usd_num*conversion_factor
rounded_pounds = round(pounds,2)
print(f"{usd_num}USD is the same as {rounded_pounds}Pounds")

#string methods
name = "lee cat"
name2 = "BOB BUILDER"
print(name.upper())
print(name.title)
print(name2.lower())
