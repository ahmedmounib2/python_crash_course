# input function
prompt = 'if you tell us who you are, we can personalize the message you see.'
prompt += "\nwhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}")

age= input('how old are you? ')
age= int(age)
if age >= 18:
    print(f"\nyour age is {age}, you are older than 18, you are allowed to join")
else:
    print("\nsorry you are less than legal age")


height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# The Modulo Operator
# A useful tool for working with numerical information is the modulo operator
# (%), which divides one number by another number and returns the
# remainder:
# >>> 4 % 3
# 1
# >>> 5 % 3
# 2
# >>> 6 % 3
# 0
# >>> 7 % 3
# 1
# The modulo operator doesn’t tell you how many times one number fits
# into another; it just tells you what the remainder is.
# When one number is divisible by another number, the remainder is 0, so
# the modulo operator always returns 0. You can use this fact to determine if a
# number is even or odd:
number= input("Enter a number and i will tell you if its evewn or odd: ")
number= int(number)

if number %2 == 0:
    print(f"\n{number} is an even number")
else:
    print(f"\n{number} is an odd number")

# Even numbers are always divisible by two, so if the modulo of a number
# and two is zero (here, if number % 2 == 0) the number is even. Otherwise, it’s
# odd.

# while loops, they run as long as a certain condition is true.
current_number= 1
while current_number <=5:
    print(current_number)
    current_number += 1

# Letting the User Choose When to Quit
# while loop to make the user decide when to quit

prompt = "\ntell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
prompt += "\nEnter your message here: "
message = ""
while message.lower() != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Using a Flag, to use While with more than one condition.

prompt = "\n tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# Using break to Exit a Loop

prompt = "\nPlease input the name of the city you were born"
prompt += "\n Enter 'quit' when you are finised "
while True:
    city= input(prompt)
    if city == 'quit':
        break
    else:
        print(f"\nI would love to go to {city.title()}!")

# Using continue in a Loop
# Rather than breaking out of a loop entirely without executing the rest of its
# code, you can use the continue statement to return to the beginning of the
# loop based on the result of a conditional test. For example, consider a loop
# that counts from 1 to 10 but prints only the odd numbers in that range:

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number %2 == 0:
        continue
    print(f"\n{current_number})
